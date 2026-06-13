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


def search_document_types(query: str, limit: int = 3, min_score: int = 0):
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
        """
        Морфологическое расширение слова: корни + типичные окончания + снятие приставок.
        Синонимы сюда НЕ добавляются — они должны быть в поле keywords документа в БД.
        """
        t = term.strip().lower()
        if len(t) < 1:
            return []
        suffixes = (
            "а", "ы", "е", "у", "ой", "ою", "и", "ов", "ом", "ам", "ах", "ами",
            "ю", "я", "к", "ки", "ке", "ку", "кой", "ий", "ого", "ому", "им", "ие", "их",
        )
        roots: set[str] = set()
        out: set[str] = {t}

        if len(t) >= 3:
            for cut in (1, 2, 3):
                root = t[:-cut]
                if len(root) < 3:
                    continue
                roots.add(root)
                out.add(root)
                for suf in suffixes:
                    out.add(root + suf)

        # Снятие приставок: по-дарить → дарить → дар и т.д.
        for pfx in ("по", "за", "на", "пере", "вы", "при", "от", "до", "об", "раз", "под", "у"):
            if t.startswith(pfx) and len(t) - len(pfx) >= 3:
                stem = t[len(pfx):]
                roots.add(stem)
                out.add(stem)
                for cut in (1, 2, 3):
                    root = stem[:-cut]
                    if len(root) >= 3:
                        roots.add(root)
                        out.add(root)
                        for suf in suffixes:
                            out.add(root + suf)

        # Корни — всегда в выборке (чтобы не обрезались лимитом)
        long_variants = sorted(
            (s for s in out if s not in roots),
            key=lambda s: (-len(s), s),
        )[:60]
        return list(roots) + long_variants

    def score_doc(doc: DocumentType) -> int:
        name = (doc.name or "").lower()
        desc = (doc.short_description or "").lower()
        keys = (doc.keywords or "").lower()
        text = " ".join([name, desc, keys])
        total = 0
        for term in terms:
            best = 0
            for variant in expand_search_tokens(term):
                if len(variant) < 3:
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
        if s >= max(1, min_score):
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


def call_openai_chat(
    user_message: str,
    timeout: float = 15.0,
    context_docs=None,       # list[DocumentType] | None
) -> str:
    q = (user_message or "").strip()
    api_key = getattr(settings, "OPENAI_API_KEY", "") or ""

    if not api_key:
        if context_docs:
            lines = [f"• {d.name}" for d in context_docs]
            return "Найдены подходящие шаблоны:\n" + "\n".join(lines)
        return (
            "Сервис ответа временно недоступен. Могу помочь с подбором шаблона договора по ключевым словам."
        )

    # Базовый системный промпт
    system = (
        "Ты — AI-помощник сервиса КЮД (конструктор юридических документов) по вопросам недвижимости и строительства в РФ. "
        "Отвечай кратко и по делу (2–5 предложений) на русском языке. "
        "Наши темы: покупка/продажа жилья, аренда, найм (снять/сдать квартиру), дарение, мена/обмен, "
        "рента, ипотека, долевое строительство, строительный подряд, права на недвижимость — всё это наши темы. "
        "Отказывай только если вопрос явно никак не связан с недвижимостью, строительством или юридическими документами. "
        "Всегда добавляй в конце: «Ответ носит справочный характер и не является юридической консультацией. "
        "Для решения конкретной ситуации обратитесь к квалифицированному юристу.»"
    )

    # Если есть релевантные шаблоны — вставляем их в промпт, чтобы LLM ссылался только на них
    if context_docs:
        doc_lines = "\n".join(f"- {d.name}" for d in context_docs)
        system += (
            f"\n\nВ нашем каталоге найдены подходящие шаблоны:\n{doc_lines}\n"
            "Если уместно — порекомендуй именно эти шаблоны (не придумывай других названий)."
        )
    else:
        system += (
            "\n\nПодходящих шаблонов в каталоге не найдено — не предлагай никаких конкретных договоров."
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
        "max_tokens": 700,
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
