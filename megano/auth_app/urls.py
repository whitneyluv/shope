from django.urls import path
from django.views.generic import TemplateView
from .views import (
    UserLoginView,
    UserLogoutView,
    UserRegisterView,
    EmailVerify,
    UserPasswordResetView,
    UserPasswordConfirmView,
)

app_name = 'auth_app'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registration/', UserRegisterView.as_view(), name='registration'),

    path('registration/confirm_email/', TemplateView.as_view(
        template_name='auth_app/registration_confirm_email.html'
    ), name='registration_confirm_email'),

    path('registration/<activation_key>/', EmailVerify.as_view(), name='registration_confirmation_email'),

    path('registration/invalid_verify/', TemplateView.as_view(
            template_name='auth_app/registration_confirm_email.html'
        ), name='registration_invalid'),

    path('reset_password/', UserPasswordResetView.as_view(), name='reset_password_request'),

    path('reset_password/confirm_email/', TemplateView.as_view(
        template_name='auth_app/confirm_email_reset_password_request.html'
    ), name='confirm_email_reset_password_request'),

    path('reset_password/<uidb64>/<token>/', UserPasswordConfirmView.as_view(), name='set_new_password'),

    path('reset_password/confirm_reset_password/', TemplateView.as_view(
        template_name='auth_app/password_reset_complete.html'
    ), name='confirm_reset_password'),

    ]
