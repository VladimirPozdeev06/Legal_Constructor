"""Чтение юридических документов (DOCX) для показа в модальном окне."""

from __future__ import annotations

from pathlib import Path

from django.conf import settings
from django.utils.html import escape


def _first_docx_in_dir(directory: Path) -> Path | None:
    if not directory.is_dir():
        return None
    for pattern in ("*.docx", "*.doc"):
        found = sorted(directory.glob(pattern))
        if found:
            return found[0]
    return None


def _pick_docx_for_slug(directory: Path, slug: str) -> Path | None:
    """Выбирает DOCX в каталоге по slug (два файла в одной папке)."""
    if not directory.is_dir():
        return None
    files = sorted(directory.glob("*.docx"))
    if not files:
        return _first_docx_in_dir(directory)

    def score(name: str, keywords: tuple[str, ...]) -> int:
        n = name.lower()
        return sum(10 for k in keywords if k in n)

    if slug == "privacy":
        keys = ("политик", "конфиденциаль", "privacy")
        ranked = sorted(files, key=lambda p: score(p.name, keys), reverse=True)
        if score(ranked[0].name, keys) > 0:
            return ranked[0]
        return files[0]

    if slug == "consent":
        keys = ("соглас", "персональн", "обработк", "consent")
        ranked = sorted(files, key=lambda p: score(p.name, keys), reverse=True)
        if score(ranked[0].name, keys) > 0:
            return ranked[0]
        if len(files) >= 2:
            return files[1]
        return files[0]

    return files[0]


def resolve_legal_doc_path(slug: str) -> Path | None:
    """Возвращает путь к файлу DOCX для slug privacy | consent."""
    mapping = getattr(settings, "LEGAL_DOCUMENT_PATHS", {})
    raw = mapping.get(slug)
    if raw is None:
        return None
    path = Path(raw)
    if path.is_file():
        return path
    if path.is_dir():
        return _pick_docx_for_slug(path, slug)
    return None


def read_docx_plain_paragraphs(path: Path) -> list[str]:
    from docx import Document

    doc = Document(str(path))
    lines: list[str] = []
    for p in doc.paragraphs:
        t = (p.text or "").strip()
        if t:
            lines.append(t)
    return lines


def paragraphs_to_safe_html(paragraphs: list[str]) -> str:
    parts = []
    for line in paragraphs:
        parts.append(f"<p>{escape(line)}</p>")
    return "\n".join(parts) if parts else "<p>Документ пуст.</p>"
