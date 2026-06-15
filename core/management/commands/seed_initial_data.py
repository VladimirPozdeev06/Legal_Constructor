from io import StringIO

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    help = "Наполняет пустую базу начальными данными (размеченные шаблоны, приложения, пользователи)."

    def handle(self, *args, **options):
        from catalog.models import TemplateVersion

        # Типы документов создаёт миграция catalog.0002; размеченные .docx-шаблоны,
        # приложения и пользователи — только в фикстуре. Грузим, если их ещё нет.
        already = (
            TemplateVersion.objects.exclude(docx_file="").exclude(docx_file=None).exists()
        )
        if already:
            self.stdout.write("Размеченные шаблоны уже загружены — пропускаю seed.")
            return

        call_command("loaddata", "seed.json")

        # Postgres: сбрасываем последовательности, чтобы новые записи (регистрации и т.п.)
        # не конфликтовали с явными PK из фикстуры.
        if connection.vendor == "postgresql":
            out = StringIO()
            call_command("sqlsequencereset", "catalog", "auth", "documents", "accounts", stdout=out)
            sql = out.getvalue().strip()
            if sql:
                with connection.cursor() as cur:
                    cur.execute(sql)
            self.stdout.write("Последовательности Postgres сброшены.")

        self.stdout.write(self.style.SUCCESS("Начальные данные (шаблоны + пользователи) загружены."))
