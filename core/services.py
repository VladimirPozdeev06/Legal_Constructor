import json
import re
import socket
import urllib.error
import urllib.request
from django.conf import settings

from catalog.models import DocumentType

VARIABLE_RE = re.compile(r"\{\{\s*([^}]+?)\s*\}\}")


def extract_variable_keys(template_body: str) -> list[str]:
    keys = []
    for m in VARIABLE_RE.finditer(template_body or ""):
        key = m.group(1).strip()
        if key and key not in keys:
            keys.append(key)
    return keys


def merge_template_body(template_body: str, values: dict[str, str]) -> str:
    def repl(match):
        key = match.group(1).strip()
        return values.get(key, match.group(0))

    return VARIABLE_RE.sub(repl, template_body or "")


def search_document_types(query: str, limit: int = 3):
    q = (query or "").strip()
    if len(q) < 2:
        return []

    terms = [t for t in re.split(r"\s+", q) if t]
    if not terms:
        return []

    base = list(
        DocumentType.objects.filter(
            domain__slug__in=["real-estate", "construction"],
            domain__is_active=True,
            is_active=True,
        ).order_by("sort_order", "name")
    )

    def expand_search_tokens(term: str) -> list[str]:
        t = term.strip().lower()
        if len(t) < 1:
            return []
        out: set[str] = {t}
        # Простая морфология: отрезаем 1–2 буквы и подставляем типичные окончания (мена→мены, рента→ренты)
        suffixes = (
            "а",
            "ы",
            "е",
            "у",
            "ой",
            "ою",
            "и",
            "ов",
            "ом",
            "ам",
            "ах",
            "ами",
            "ю",
            "я",
            "к",
            "ки",
            "ке",
            "ку",
            "кой",
            "ий",
            "ого",
            "ому",
            "им",
            "ом",
            "ие",
            "их",
        )
        if len(t) >= 3:
            for cut in (1, 2):
                root = t[:-cut]
                if len(root) < 2:
                    continue
                out.add(root)
                for suf in suffixes:
                    out.add(root + suf)
        # Ограничиваем комбинаторный взрыв
        ranked = sorted(out, key=lambda s: (-len(s), s))
        return ranked[:48]

    def score_doc(doc: DocumentType) -> int:
        name = (doc.name or "").lower()
        desc = (doc.short_description or "").lower()
        keys = (doc.keywords or "").lower()
        text = " ".join([name, desc, keys])
        total = 0
        for term in terms:
            best = 0
            for variant in expand_search_tokens(term):
                if len(variant) < 2:
                    continue
                if variant in name:
                    best = max(best, 14 + min(len(variant), 12))
                elif variant in desc or variant in keys:
                    best = max(best, 8)
                elif variant in text:
                    best = max(best, 4)
            total += best
        return total

    scored: list[tuple[int, DocumentType]] = []
    for doc in base:
        s = score_doc(doc)
        if s > 0:
            scored.append((s, doc))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [d for _, d in scored[:limit]]


PROFANITY_MARKERS = ("хуй", "пизд", "еба", "бля", "сука")


def is_profanity_or_gibberish(text: str) -> bool:
    tl = (text or "").lower()
    if len(tl.strip()) < 3:
        return True
    for w in PROFANITY_MARKERS:
        if w in tl:
            return True
    if re.fullmatch(r"[\W\d_]+", tl):
        return True
    return False


DOCUMENT_INTENT_MARKERS = (
    "договор",
    "договора",
    "документ",
    "шаблон",
    "бланк",
    "образец",
    "купли",
    "продажи",
    "дарения",
    "аренды",
    "ренты",
    "найма",
    "ипотеки",
    "цессии",
)


def is_document_request(text: str) -> bool:
    q = (text or "").lower().strip()
    if not q:
        return False
    return any(marker in q for marker in DOCUMENT_INTENT_MARKERS)


def call_openai_chat(user_message: str, timeout: float = 15.0) -> str:
    q = (user_message or "").strip()
    api_key = getattr(settings, "OPENAI_API_KEY", "") or ""

    if not api_key:
        if is_document_request(q):
            docs = search_document_types(q, limit=5)
            if docs:
                lines = [f"• {d.name}" for d in docs]
                return "Найдены подходящие шаблоны:\n" + "\n".join(lines)
        return (
            "Сервис ответа временно недоступен. Могу помочь с подбором шаблона договора по ключевым словам."
        )

    system = (
        "Ты — AI-помощник сервиса КЮД (конструктор юридических документов) по вопросам недвижимости и строительства в РФ. "
        "Отвечай кратко и по делу (2-5 предложений) на русском языке. "
        "Если пользователь ищет договор или шаблон — назови до 3 подходящих из нашего каталога (купля-продажа, дарение, мена, рента, найм и др.). "
        "Всегда добавляй в конце ответа: «Ответ носит справочный характер и не является юридической консультацией. "
        "Для решения конкретной ситуации обратитесь к квалифицированному юристу.» "
        "Если вопрос не связан с недвижимостью или строительством — вежливо откажись отвечать."
    )

    base_url = getattr(settings, "OPENAI_BASE_URL", "https://openrouter.ai/api/v1").rstrip("/")
    model = getattr(settings, "OPENAI_MODEL", "meta-llama/llama-3.1-8b-instruct:free")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": q},
        ],
        "temperature": 0.4,
        "max_tokens": 400,
    }

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=data,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, socket.timeout):
        raise TimeoutError("LLM unavailable")
    except json.JSONDecodeError as exc:
        raise TimeoutError("LLM bad response") from exc

    try:
        return body["choices"][0]["message"]["content"].strip()
    except (KeyError, IndexError, TypeError) as exc:
        raise TimeoutError("LLM parse error") from exc
