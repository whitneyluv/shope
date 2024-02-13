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
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('verify_email/<activation_key>/', EmailVerify.as_view(), name='verify_email'),

    path('confirm_email/', TemplateView.as_view(
        template_name='auth_app/confirm_email_account_registration.html'
    ), name='confirm_email_account_registration'),

    path('reset_password/', UserPasswordResetView.as_view(), name='reset_password_request'),

    path('reset_password/confirm_email/', TemplateView.as_view(
        template_name='auth_app/confirm_email_reset_password_request.html'
    ), name='confirm_email_reset_password_request'),

    path('reset_password/<uidb64>/<token>/', UserPasswordConfirmView.as_view(), name='set_new_password'),

    path('reset_password/confirm_reset_password/', TemplateView.as_view(
        template_name='auth_app/password_reset_complete.html'
    ), name='confirm_reset_password'),

    ]
