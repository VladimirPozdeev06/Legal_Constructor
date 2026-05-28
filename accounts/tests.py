from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class AuthFlowTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)

    def test_register_creates_user_and_redirects_to_cabinet(self):
        response = self.client.post(
            reverse("accounts:register"),
            data={
                "email": "newuser@example.com",
                "password": "abc12",
                "password_confirm": "abc12",
                "accepted_terms": True,
            },
        )
        self.assertRedirects(response, reverse("core:cabinet"))
        self.assertTrue(User.objects.filter(email="newuser@example.com").exists())

    def test_login_redirects_to_cabinet(self):
        User.objects.create_user(
            username="user@example.com",
            email="user@example.com",
            password="abc12",
        )
        response = self.client.post(
            reverse("accounts:login"),
            data={"username": "user@example.com", "password": "abc12"},
        )
        self.assertRedirects(response, reverse("core:cabinet"))

    def test_login_is_case_insensitive_by_email(self):
        User.objects.create_user(
            username="MixedCase@Example.com",
            email="MixedCase@Example.com",
            password="abc12",
        )
        response = self.client.post(
            reverse("accounts:login"),
            data={"username": "mixedcase@example.com", "password": "abc12"},
        )
        self.assertRedirects(response, reverse("core:cabinet"))

    def test_cabinet_requires_authentication(self):
        response = self.client.get(reverse("core:cabinet"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("accounts:login"), response.url)

    def test_register_accepts_password_with_length_30(self):
        response = self.client.post(
            reverse("accounts:register"),
            data={
                "email": "maxlen@example.com",
                "password": "a" * 29 + "1",
                "password_confirm": "a" * 29 + "1",
                "accepted_terms": True,
            },
        )
        self.assertRedirects(response, reverse("core:cabinet"))

    def test_register_rejects_password_longer_than_30(self):
        response = self.client.post(
            reverse("accounts:register"),
            data={
                "email": "toolong@example.com",
                "password": "a" * 30 + "1",
                "password_confirm": "a" * 30 + "1",
                "accepted_terms": True,
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "at most 30 characters")
