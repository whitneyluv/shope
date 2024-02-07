from django.contrib.auth.views import LoginView


class UserLoginView(LoginView):
    """
    View функция отображения страницы логирования на сайт
    """
    template_name = 'auth_app/login.html'
    redirect_authenticated_user = True
    next_page = '/profile/'
