from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views import View

from .forms import EmailAuthenticationForm, RegisterForm


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    authentication_form = EmailAuthenticationForm
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "Неверный email или пароль. Попробуйте снова")
        return super().form_invalid(form)


class UserRegisterView(View):
    template_name = "accounts/register.html"

    def get(self, request):
        return render(request, self.template_name, {"form": RegisterForm()})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            created_user = self._create_user(user, password)
            login(request, created_user, backend="accounts.backends.EmailBackend")
            return redirect("core:cabinet")
        return render(request, self.template_name, {"form": form})

    @staticmethod
    def _create_user(email, password):
        from django.contrib.auth import get_user_model

        user_model = get_user_model()
        return user_model.objects.create_user(
            username=email,
            email=email,
            password=password,
        )


class UserLogoutView(LogoutView):
    pass
