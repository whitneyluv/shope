from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'auth_app/login.html'
    redirect_authenticated_user = True
    next_page = '/profile/'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('auth_app:login')
