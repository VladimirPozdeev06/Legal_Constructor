import json
import re
import socket
import time
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
    # сам документ
    "договор", "документ", "шаблон", "бланк", "образец", "соглашен", "оферт",
    # намерение оформить/получить документ
    "оформ", "состав", "заключ", "заполн", "скача", "подписа",
    # типы сделок / действия, для которых нужен документ
    "куп", "прода", "покуп",
    "дарен", "подари", "дарит",
    "аренд", "сдат", "снят", "найм", "наним",
    "рент", "ипотек", "залог", "цесси", "уступк", "обмен", "подряд", "долев",
)


# Явное намерение получить/оформить документ — перевешивает информационные маркеры
# («как оформить договор ренты» → шаблоны нужны, хотя начинается с «как»).
DOCUMENT_ACTION_MARKERS = (
    "оформ", "состав", "заключ", "заполн", "скача", "подписа", "сформир",
    "подготов", "сделай", "создай", "помоги составить", "помоги оформить",
    "хочу договор", "хочу оформить", "хочу составить", "хочу заключить",
    "дай шаблон", "дай образец", "дай бланк", "где шаблон", "где скача",
)
# Примечание: «нужен договор/документ» намеренно НЕ здесь — иначе «зачем нужен
# договор найма» (информационный вопрос) ошибочно считался бы намерением оформить.
# Такие фразы и так дают шаблоны через общий список DOCUMENT_INTENT_MARKERS ниже,
# но проигрывают информационным маркерам («зачем нуж…»).

# Признаки чисто информационного/толкового вопроса — на них шаблоны не навязываем,
# даже если упомянут тип документа («что такое рента?», «чем отличается дарение от купли-продажи?»).
INFO_QUESTION_MARKERS = (
    "что такое", "что это", "что значит", "что означает", "что подразумева",
    "чем отлич", "в чем отлич", "в чём отлич", "в чем разниц", "в чём разниц",
    "разница между", "отличие", "отличия", "объясни", "поясни", "расскажи",
    "что лучше", "как работает", "как устроен", "зачем нуж", "для чего нуж",
    "почему", "какие бывают", "какие виды", "кто такой", "кто такая",
    "правда ли", "можно ли", "нужно ли", "обязательно ли", "законно ли",
)


def is_document_request(text: str) -> bool:
    q = (text or "").lower().strip()
    if not q:
        return False
    # Явное намерение оформить документ — всегда предлагаем шаблоны.
    if any(m in q for m in DOCUMENT_ACTION_MARKERS):
        return True
    # Тип документа/сделки вообще не упомянут — точно не предлагаем.
    if not any(marker in q for marker in DOCUMENT_INTENT_MARKERS):
        return False
    # Документ упомянут, но это толковый/информационный вопрос без намерения оформить —
    # шаблоны не навязываем (отвечаем текстом).
    if any(m in q for m in INFO_QUESTION_MARKERS):
        return False
    return True


# Вопрос-перечисление каталога: «какие договоры есть?», «что вы умеете»,
# «список документов» и т.п. — нужно показать реальный каталог карточками.
CATALOG_LISTING_MARKERS = (
    "что вы умеете", "что ты умеешь", "что умеешь", "что вы можете", "что можете",
    "что можешь", "чем можешь помочь", "чем вы помогаете", "что у вас есть",
    "что есть у вас", "что предлагаете", "что вы предлагаете",
    "список договор", "список документ", "список шаблон",
    "перечисли договор", "перечисли документ", "перечисли шаблон",
    "покажи договор", "покажи документ", "покажи шаблон", "покажи список",
    "какие договор", "какие документ", "какие шаблон", "какие бланк", "какие сделк",
    "что можно оформить", "что можно составить", "что можно заполнить",
    "что можно сделать", "какие услуги",
)
# Устойчивый к опечаткам шаблон «какие <что-то> есть/бывают/доступны»
# (ловит и «какие догворы есть», и «какие документы имеются»).
_LISTING_RE = re.compile(r"как(?:ие|их|ой)\s+\S+\s+(?:есть|бывают|имеются|доступн|предусмотрен)")


def is_catalog_listing_question(text: str) -> bool:
    q = (text or "").lower().strip()
    if not q:
        return False
    if any(m in q for m in CATALOG_LISTING_MARKERS):
        return True
    return bool(_LISTING_RE.search(q))


def list_catalog_documents(limit: int = 8):
    """Реальный каталог доступных типов документов (для вопросов-перечислений)."""
    return list(
        DocumentType.objects.filter(
            domain__slug__in=["real-estate", "construction"],
            domain__is_active=True,
            is_active=True,
        ).order_by("sort_order", "name")[:limit]
    )


# Рекомендуемая цепочка по умолчанию (если переменная OPENAI_MODELS не задана):
# сначала быстрая и качественная gpt-oss-20b, затем маленькая llama как быстрый
# запас. Настроенная OPENAI_MODEL добавляется последним резервом (см. ниже).
DEFAULT_MODELS = (
    "openai/gpt-oss-20b:free",
    "meta-llama/llama-3.2-3b-instruct:free",
)

# Ошибки одной модели, при которых имеет смысл пробовать следующую.
_MODEL_RETRYABLE_ERRORS = (
    urllib.error.HTTPError,
    urllib.error.URLError,
    TimeoutError,
    socket.timeout,
    json.JSONDecodeError,
    KeyError,
    IndexError,
    TypeError,
    ValueError,
)


def resolve_chat_models() -> list[str]:
    """Список моделей для failover-цепочки (в порядке приоритета, без дублей)."""
    raw = (getattr(settings, "OPENAI_MODELS", "") or "").strip()
    if raw:
        models = [m.strip() for m in raw.replace("\n", ",").split(",") if m.strip()]
    else:
        models = list(DEFAULT_MODELS)
        primary = (getattr(settings, "OPENAI_MODEL", "") or "").strip()
        if primary:
            models.append(primary)  # настроенная модель — последним резервом
    seen, out = set(), []
    for m in models:
        if m not in seen:
            seen.add(m)
            out.append(m)
    return out


def _request_single_model(model, system, q, base_url, api_key, timeout) -> str:
    """Один запрос к конкретной модели. Бросает исключение при ошибке/пустом ответе."""
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
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    content = (body["choices"][0]["message"]["content"] or "").strip()
    if not content:
        raise ValueError("empty answer")
    return content


def call_openai_chat(
    user_message: str,
    timeout: float = 22.0,            # общий бюджет на всю цепочку моделей
    context_docs=None,               # list[DocumentType] | None
    per_model_timeout: float = 8.0,  # сколько ждём каждую модель, прежде чем перейти к следующей
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
        "НЕ добавляй в конце дисклеймер про «справочный характер» или «обратитесь к юристу» — "
        "такая приписка уже показывается под ответом отдельно. Заканчивай ответ по сути вопроса."
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
    models = resolve_chat_models()

    # Пробуем модели по очереди: первая, что ответит, — выигрывает. Если модель
    # долго молчит или вернула ошибку (429/503 и т.п.) — переходим к следующей.
    # Общий бюджет времени ограничен, чтобы запрос не висел дольше нужного.
    deadline = time.monotonic() + timeout
    last_exc = None
    for model in models:
        remaining = deadline - time.monotonic()
        if remaining < 2:
            break
        try:
            return _request_single_model(
                model, system, q, base_url, api_key, min(per_model_timeout, remaining)
            )
        except _MODEL_RETRYABLE_ERRORS as exc:
            last_exc = exc
            continue

    raise TimeoutError(f"LLM unavailable ({last_exc})")
