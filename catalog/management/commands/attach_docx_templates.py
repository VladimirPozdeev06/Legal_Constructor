"""
Прикрепляет размеченные .docx файлы к TemplateVersion в БД.

Использование:
    python manage.py attach_docx_templates --srcdir "C:\\путь\\к\\Шаблоны с разметкой"

Если --srcdir не указан, ищет папку по дефолтному пути.
Для каждого файла с суффиксом __РАЗМЕТКА.docx команда:
1. Находит DocumentType по ключевому слову из имени файла
2. Берёт последнюю опубликованную TemplateVersion
3. Копирует файл в media/templates/docx/ и сохраняет путь в docx_file
"""

import shutil
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from catalog.models import DocumentType, TemplateVersion

# Маппинг: подстрока в имени файла → подстрока для поиска DocumentType (icontains)
FILE_TO_DOCTYPE = [
    ("купли-продажи",       "купли-продажи"),
    ("мены жилых",          "мены"),
    ("краткосрочного найма","краткосрочного"),
    ("безвозмездного",      "безвозмездного"),
    ("найма жилого",        "найма жилого"),     # коммерческий
]

DEFAULT_SRCDIR = (
    Path(settings.BASE_DIR).parent
    / "Проект КЮД"
    / "Шаблоны"
    / "Шаблоны с разметкой"
)


class Command(BaseCommand):
    help = "Привязывает размеченные .docx к TemplateVersion (поле docx_file)"

    def add_arguments(self, parser):
        parser.add_argument(
            "--srcdir",
            type=str,
            default=str(DEFAULT_SRCDIR),
            help="Папка с размеченными __РАЗМЕТКА.docx файлами",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Только показать что будет сделано, без изменений",
        )

    def handle(self, *args, **options):
        srcdir = Path(options["srcdir"])
        dry_run = options["dry_run"]

        if not srcdir.is_dir():
            raise CommandError(f"Папка не найдена: {srcdir}")

        # Собираем все *__РАЗМЕТКА.docx рекурсивно
        marked_files = sorted(srcdir.rglob("*__РАЗМЕТКА.docx"))
        if not marked_files:
            self.stderr.write(self.style.WARNING(f"В папке нет файлов __РАЗМЕТКА.docx: {srcdir}"))
            return

        self.stdout.write(f"Найдено файлов: {len(marked_files)}\n")

        media_dest = Path(settings.MEDIA_ROOT) / "templates" / "docx"
        if not dry_run:
            media_dest.mkdir(parents=True, exist_ok=True)

        attached = 0
        skipped = 0

        for src_path in marked_files:
            fname = src_path.name.lower()

            # Находим подходящий DocumentType
            doc_type = None
            for keyword_file, keyword_db in FILE_TO_DOCTYPE:
                if keyword_file.lower() in fname:
                    doc_type = (
                        DocumentType.objects
                        .filter(name__icontains=keyword_db, is_active=True)
                        .first()
                    )
                    if doc_type:
                        break

            if doc_type is None:
                self.stderr.write(
                    self.style.WARNING(f"  [skip] No DocumentType found for: {src_path.name}")
                )
                skipped += 1
                continue

            # Последняя опубликованная версия
            tv = (
                TemplateVersion.objects
                .filter(
                    template__document_type=doc_type,
                    template__is_active=True,
                    is_published=True,
                )
                .order_by("-version_number")
                .first()
            )
            if tv is None:
                self.stderr.write(
                    self.style.WARNING(
                        f"  [skip] No published TemplateVersion for {doc_type.name!r}"
                    )
                )
                skipped += 1
                continue

            # Имя файла в media: <slug>_v<ver>__RAZMETKA.docx
            dest_name = f"{doc_type.slug}_v{tv.version_number}__razmetka.docx"
            dest_path = media_dest / dest_name
            relative = Path("templates") / "docx" / dest_name

            prefix = "[DRY] " if dry_run else ""
            self.stdout.write(
                f"  {prefix}{doc_type.name!r} -> {dest_name}"
            )

            if not dry_run:
                shutil.copy2(src_path, dest_path)
                tv.docx_file = str(relative)
                tv.save(update_fields=["docx_file"])

            attached += 1

        if dry_run:
            self.stdout.write(
                self.style.WARNING(
                    f"\nDry run: {attached} to attach, {skipped} skipped."
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"\nDone: {attached} attached, {skipped} skipped."
                )
            )
