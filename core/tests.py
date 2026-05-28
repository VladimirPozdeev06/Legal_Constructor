from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.models import DocumentType, LegalDomain, Template, TemplateVersion
from documents.models import UserDocument

User = get_user_model()


class CabinetCatalogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="test@example.com",
            email="test@example.com",
            password="abc12",
        )
        self.domain, _ = LegalDomain.objects.get_or_create(
            slug="real-estate",
            defaults={"name": "Недвижимость", "is_active": True, "sort_order": 1},
        )
        self.doc_type, _ = DocumentType.objects.get_or_create(
            domain=self.domain,
            slug="purchase-sale-residential",
            defaults={
                "name": "Договор купли-продажи жилого помещения",
                "is_active": True,
                "sort_order": 1,
            },
        )
        template, _ = Template.objects.get_or_create(
            document_type=self.doc_type,
            defaults={"title": "Шаблон аренды", "is_active": True},
        )
        self.version, _ = TemplateVersion.objects.get_or_create(
            template=template,
            version_number=1,
            defaults={"body": "body", "is_published": True},
        )

    def test_cabinet_shows_catalog_from_db(self):
        self.client.login(username="test@example.com", password="abc12")
        response = self.client.get(reverse("core:cabinet"))
        self.assertContains(response, "Недвижимость")
        self.assertContains(response, "Договор купли-продажи жилого помещения")

    def test_start_document_creates_draft(self):
        self.client.login(username="test@example.com", password="abc12")
        response = self.client.get(
            reverse("core:start_document", args=[self.doc_type.id])
        )
        self.assertEqual(response.status_code, 302)
        ud = UserDocument.objects.get(user=self.user)
        self.assertIn(reverse("core:cabinet"), response["Location"])
        self.assertIn(f"doc={ud.id}", response["Location"])
        self.assertIn("domain=", response["Location"])

    def test_download_template_docx_returns_docx(self):
        self.client.login(username="test@example.com", password="abc12")
        response = self.client.get(
            reverse("core:download_template_docx", args=[self.doc_type.id])
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"],
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )
