from django.urls import path
from django.views.generic import TemplateView
from .views import UserLoginView, UserLogoutView, RegisterListView, EmailVerify

app_name = 'auth_app'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('password_recovery/', TemplateView.as_view(template_name='auth_app/email.html'), name='password_recovery'),
    path('email/password/', TemplateView.as_view(template_name='auth_app/password.html'), name='password'),
    path('verify_email/<activation_key>/', EmailVerify.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(template_name='auth_app/confirm_email.html'), name='confirm_email'),
    ]
