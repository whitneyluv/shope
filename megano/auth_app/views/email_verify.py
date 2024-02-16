from django.views import View
from django.shortcuts import redirect
import inject
from ..interfaces.auth_interface import IAuth
from django.contrib.auth import login
from profile_app.models import Profile


class EmailVerify(View):
    """
    View функция отображения страницы завершения регистрации
    """
    _user: IAuth = inject.attr(IAuth)

    def get(self, request, activation_key):
        user = self._user.get_user_by_activation_key(activation_key)
        if user is not None:
            self._user.set_user_is_active(user, True)
            self._user.save(user)
            login(request, user)
            return redirect('auth_app:login')
        return redirect('/auth/registration/invalid_verify/')
