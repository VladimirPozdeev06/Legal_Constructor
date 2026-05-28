from django.db import migrations


def seed_catalog(apps, schema_editor):
    LegalDomain = apps.get_model("catalog", "LegalDomain")
    DocumentType = apps.get_model("catalog", "DocumentType")
    Template = apps.get_model("catalog", "Template")
    TemplateVersion = apps.get_model("catalog", "TemplateVersion")

    real_estate, _ = LegalDomain.objects.get_or_create(
        slug="real-estate",
        defaults={"name": "Недвижимость", "is_active": True, "sort_order": 1},
    )
    construction, _ = LegalDomain.objects.get_or_create(
        slug="construction",
        defaults={"name": "Строительство", "is_active": True, "sort_order": 2},
    )
    family, _ = LegalDomain.objects.get_or_create(
        slug="family-law",
        defaults={"name": "Семейное право", "is_active": False, "sort_order": 3},
    )

    docs_to_create = [
        (
            real_estate,
            "purchase-sale-residential",
            "Договор купли-продажи жилого помещения",
            "Сделка по покупке/продаже квартиры или дома",
            "квартира, дом, купля-продажа, недвижимость",
            True,
            1,
        ),
        (
            real_estate,
            "rental-residential",
            "Договор аренды жилого помещения",
            "Передача жилого помещения во временное пользование",
            "аренда, найм, квартира",
            True,
            2,
        ),
        (
            construction,
            "construction-contract",
            "Договор строительного подряда",
            "Выполнение строительных работ подрядчиком",
            "подряд, строительство, смета",
            True,
            1,
        ),
        (
            family,
            "marriage-contract",
            "Брачный договор",
            "Заглушка для неактивной отрасли",
            "семья, брак",
            False,
            1,
        ),
    ]

    for domain, slug, name, description, keywords, is_active, order in docs_to_create:
        document_type, _ = DocumentType.objects.get_or_create(
            domain=domain,
            slug=slug,
            defaults={
                "name": name,
                "short_description": description,
                "keywords": keywords,
                "is_active": is_active,
                "sort_order": order,
            },
        )
        template, _ = Template.objects.get_or_create(
            document_type=document_type,
            title=f"Шаблон: {name}",
            defaults={"is_active": True},
        )
        TemplateVersion.objects.get_or_create(
            template=template,
            version_number=1,
            defaults={
                "body": (
                    f"{name}\n\n"
                    "Сторона 1: {{party_one}}\n"
                    "Сторона 2: {{party_two}}\n"
                    "Предмет: {{subject}}\n"
                    "Дата: {{date}}\n"
                ),
                "is_published": is_active,
            },
        )


def clear_catalog(apps, schema_editor):
    TemplateVersion = apps.get_model("catalog", "TemplateVersion")
    Template = apps.get_model("catalog", "Template")
    DocumentType = apps.get_model("catalog", "DocumentType")
    LegalDomain = apps.get_model("catalog", "LegalDomain")

    TemplateVersion.objects.all().delete()
    Template.objects.all().delete()
    DocumentType.objects.all().delete()
    LegalDomain.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_catalog, clear_catalog),
    ]
