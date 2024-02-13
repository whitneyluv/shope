from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy


class UserPasswordResetView(PasswordResetView):
    """
    View функция отображения страницы восстановления пароля
    """
    template_name = 'auth_app/password_reset_request.html'
    success_url = reverse_lazy("auth_app:confirm_email_reset_password_request")
    email_template_name = "auth_app/password_reset_verification_cod_email.html"
