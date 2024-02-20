import inject
from ..interfaces.auth_interface import IAuth
from django.views import View
from django.shortcuts import redirect, render
from django.http import HttpRequest
from ..utils import send_email_for_verify


class ResendActivationKey(View):

    _user: IAuth = inject.attr(IAuth)

    def get(self, request: HttpRequest, activation_key: str):
        return render(request=request, template_name='auth_app/registration_activation_key_expires.html')

    def post(self, request: HttpRequest, activation_key: str):
        user = self._user.get_user_by_activation_key(activation_key)
        self._user.set_activation_key(user)
        self._user.set_activation_key_will_expires(user)
        send_email_for_verify(request, user)
        return redirect('confirm_email/')

