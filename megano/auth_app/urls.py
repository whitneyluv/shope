from django.urls import path
from django.views.generic import TemplateView
from .views import UserLoginView, UserLogoutView

app_name = 'auth_app'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('registr/', TemplateView.as_view(template_name='auth_app/registr.html'), name='registr'),
    path('email/', TemplateView.as_view(template_name='auth_app/email.html'), name='email'),
    path('email/password/', TemplateView.as_view(template_name='auth_app/password.html'), name='password'),
    ]
