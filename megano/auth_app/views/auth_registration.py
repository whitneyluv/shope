import inject


from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView


from ..interfaces.auth_interface import IAuth
from ..models.user import User


class RegisterView(FormView):

    _user: IAuth = inject.attr(IAuth)



    def get(self, request, *args, **kwargs) -> HttpResponse:


        email = request.POST['email']

        # получили пользователя
        get_user = self._user.get_user_by_email(_email=email)

        # удалили пользователя
        self._user.delete_user_by_email(_email=email)

        user_without_commit = User(
            email='test@mail.ru',
            password='12345678',
            password2='12345678',
            first_name='Nikolai',
            last_name='Nagornyi'
          )
        self._user.save(user_without_commit)

        

