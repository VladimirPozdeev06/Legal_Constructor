from django.db import migrations


REAL_ESTATE_DOCS = [
    "Договор купли-продажи жилого помещения",
    "Договор мены жилых помещений",
    "Договор дарения жилого помещения",
    "Договор ренты (постоянной, пожизненной)",
    "Договор пожизненного содержания с иждивением",
    "Договор уступки прав требования (цессии) по ДДУ",
    "Договор купли-продажи жилого помещения с рассрочкой платежа",
    "Договор социального найма жилого помещения",
    "Договор найма жилого помещения (коммерческий наем)",
    "Договор найма специализированного жилого помещения (служебное жилье, общежитие и др.)",
    "Договор поднайма жилого помещения",
    "Договор безвозмездного пользования жилым помещением (ссуды)",
    "Договор аренды жилого помещения (для юридических лиц — только для проживания граждан)",
    "Договор краткосрочного найма (до 1 года)",
    "Договор доверительного управления жилым помещением",
    "Договор ипотеки (залога) жилого помещения",
    "Договор пожизненного проживания",
    "Договор о предоставлении жилого помещения в пользование членам семьи собственника",
    "Договор об определении порядка пользования жилым помещением (между сособственниками)",
    "Соглашение о разделе (выделе долей) жилого помещения",
    "Договор обмена жилыми помещениями (между нанимателями по договору соцнайма)",
    "Договор ренты с условием пожизненного проживания",
    "Договор купли-продажи жилого помещения с условием пожизненного проживания продавца",
]


def seed_mvp_catalog(apps, schema_editor):
    LegalDomain = apps.get_model("catalog", "LegalDomain")
    DocumentType = apps.get_model("catalog", "DocumentType")
    Template = apps.get_model("catalog", "Template")
    TemplateVersion = apps.get_model("catalog", "TemplateVersion")

    real_estate, _ = LegalDomain.objects.update_or_create(
        slug="real-estate",
        defaults={"name": "Недвижимость", "is_active": True, "sort_order": 1},
    )
    construction, _ = LegalDomain.objects.update_or_create(
        slug="construction",
        defaults={"name": "Строительство", "is_active": True, "sort_order": 2},
    )

    LegalDomain.objects.exclude(id__in=[real_estate.id, construction.id]).delete()

    for index, doc_name in enumerate(REAL_ESTATE_DOCS, start=1):
        doc_type, _ = DocumentType.objects.update_or_create(
            domain=real_estate,
            slug=f"real-estate-doc-{index}",
            defaults={
                "name": doc_name,
                "short_description": "Шаблон договора для MVP-каталога недвижимости",
                "keywords": "недвижимость, жилые помещения, договор",
                "is_active": True,
                "sort_order": index,
            },
        )
        template, _ = Template.objects.get_or_create(
            document_type=doc_type,
            defaults={"title": f"Шаблон: {doc_name}", "is_active": True},
        )
        TemplateVersion.objects.get_or_create(
            template=template,
            version_number=1,
            defaults={
                "body": (
                    f"{doc_name}\n\n"
                    "Сторона 1: {{party_one}}\n"
                    "Сторона 2: {{party_two}}\n"
                    "Предмет: {{subject}}\n"
                    "Дата: {{date}}\n"
                ),
                "is_published": True,
            },
        )

    construction_doc, _ = DocumentType.objects.update_or_create(
        domain=construction,
        slug="construction-contract",
        defaults={
            "name": "Договор строительного подряда",
            "short_description": "Выполнение строительных работ подрядчиком",
            "keywords": "подряд, строительство, смета",
            "is_active": True,
            "sort_order": 1,
        },
    )
    template, _ = Template.objects.get_or_create(
        document_type=construction_doc,
        defaults={"title": "Шаблон: Договор строительного подряда", "is_active": True},
    )
    TemplateVersion.objects.get_or_create(
        template=template,
        version_number=1,
        defaults={
            "body": (
                "Договор строительного подряда\n\n"
                "Заказчик: {{party_one}}\n"
                "Подрядчик: {{party_two}}\n"
                "Объект: {{subject}}\n"
                "Дата: {{date}}\n"
            ),
            "is_published": True,
        },
    )


def noop_reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0002_seed_mvp_catalog"),
    ]

    operations = [
        migrations.RunPython(seed_mvp_catalog, noop_reverse),
    ]
