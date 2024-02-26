import inject
from django.views import View
from django.shortcuts import redirect
from django.http import HttpRequest
from ..interfaces.auth_interface import IAuth
from django.contrib.auth import login
from datetime import date, timedelta


class EmailVerify(View):
    """
    View функция отображения страницы завершения регистрации
    """
    _user: IAuth = inject.attr(IAuth)

    def get(self, request: HttpRequest, activation_key: str):
        user = self._user.get_user_by_activation_key(activation_key)
        if user:
            if date.today() > user.activation_key_will_expires:
                return redirect('activation_key_expires/')

            user.is_active = True
            self._user.save(user)
            login(request, user)
            return redirect('/profile/')

        return redirect('/auth/registration/invalid_verify/')
