import re

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "example@example.example",
                "class": (
                    "w-full h-14 rounded-lg border border-[#C6BCAC] "
                    "bg-gradient-to-t from-[#EEE8E0] to-[#F9F7F5] "
                    "px-4 text-[18px] leading-[1.3] text-[#022E4C] "
                    "placeholder:text-[#E2D9CB] focus:outline-none "
                    "focus:ring-2 focus:ring-[#517493]/35"
                ),
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].widget = forms.PasswordInput(
            attrs={
                "placeholder": "Введите ваш пароль",
                "minlength": 5,
                "maxlength": 30,
                "class": (
                    "w-full h-14 rounded-lg border border-[#C6BCAC] "
                    "bg-gradient-to-t from-[#EEE8E0] to-[#F9F7F5] "
                    "px-4 pr-14 text-[18px] leading-[1.3] text-[#022E4C] "
                    "placeholder:text-[#E2D9CB] focus:outline-none "
                    "focus:ring-2 focus:ring-[#517493]/35"
                ),
            }
        )


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label="E-mail *",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "example@example.example",
                "class": (
                    "w-full h-14 rounded-lg border border-[#C6BCAC] "
                    "bg-gradient-to-t from-[#EEE8E0] to-[#F9F7F5] "
                    "px-4 text-[18px] leading-[1.3] text-[#022E4C] "
                    "placeholder:text-[#E2D9CB] focus:outline-none "
                    "focus:ring-2 focus:ring-[#517493]/35"
                ),
            }
        ),
    )
    password = forms.CharField(
        label="Пароль",
        min_length=5,
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Не менее 5 латинских букв и цифр",
                "minlength": 5,
                "maxlength": 128,
                "class": (
                    "w-full h-14 rounded-lg border border-[#C6BCAC] "
                    "bg-gradient-to-t from-[#EEE8E0] to-[#F9F7F5] "
                    "px-4 pr-14 text-[18px] leading-[1.3] text-[#022E4C] "
                    "placeholder:text-[#E2D9CB] focus:outline-none "
                    "focus:ring-2 focus:ring-[#517493]/35"
                ),
            }
        ),
    )
    password_confirm = forms.CharField(
        label="Подтвердите пароль",
        min_length=5,
        max_length=128,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Введите пароль еще раз",
                "minlength": 5,
                "maxlength": 128,
                "class": (
                    "w-full h-14 rounded-lg border border-[#C6BCAC] "
                    "bg-gradient-to-t from-[#EEE8E0] to-[#F9F7F5] "
                    "px-4 pr-14 text-[18px] leading-[1.3] text-[#022E4C] "
                    "placeholder:text-[#E2D9CB] focus:outline-none "
                    "focus:ring-2 focus:ring-[#517493]/35"
                ),
            }
        ),
    )
    accepted_terms = forms.BooleanField(
        label="Я принимаю политику конфиденциальности и публичную оферту",
        required=True,
        error_messages={"required": "Необходимо принять политику и оферту."},
        widget=forms.CheckboxInput(
            attrs={
                "class": (
                    "h-6 w-6 shrink-0 rounded border border-[#C6BCAC] "
                    "bg-gradient-to-t from-[#EEE8E0] to-[#F9F7F5] accent-[#56061D]"
                ),
                "form": "register-form",
            }
        ),
    )

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Пользователь с таким email уже зарегистрирован. Выполните вход."
            )
        return email

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 5:
            raise forms.ValidationError("Длина пароля должна быть не менее 5 символов.")
        if not re.fullmatch(r"[A-Za-z0-9]+", password):
            raise forms.ValidationError("Допустимы только латинские буквы и цифры.")
        if not re.search(r"[A-Za-z]", password):
            raise forms.ValidationError("Пароль должен содержать хотя бы одну букву.")
        if not re.search(r"\d", password):
            raise forms.ValidationError("Пароль должен содержать хотя бы одну цифру.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Пароли не совпадают")
        return cleaned_data
