from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic import FormView
from ..models import User
from ..utils import send_email_for_verify
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class UserRegisterView(UserPassesTestMixin, FormView):

    """
    View функция регистрации пользователя
    """

    def test_func(self):
        if self.request.user.is_authenticated:
            raise PermissionDenied
        return True

    model = User
    template_name = 'auth_app/register.html'

    def post(self, request: HttpRequest, *args, **kwargs) -> HttpRequest:
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_email_for_verify(request, user)
            return redirect('/auth/confirm_email_account_registration')
        return render(
            request=request,
            template_name=self.template_name,
            context={'form': form}
        )
