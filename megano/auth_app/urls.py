from django.urls import path
from django.views.generic import TemplateView

app_name = 'auth_app'

urlpatterns = [
    path('login/', TemplateView.as_view(template_name='auth_app/login.html'), name='login'),
    path('registr/', TemplateView.as_view(template_name='auth_app/registr.html'), name='registr'),
    path('email/', TemplateView.as_view(template_name='auth_app/email.html'), name='email'),
    path('email/password/', TemplateView.as_view(template_name='auth_app/password.html'), name='password'),
    ]
