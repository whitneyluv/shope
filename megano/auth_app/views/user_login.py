import inject
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from profile_app.interfaces import IProfile


class UserLoginView(LoginView):
    """
    View функция отображения страницы логирования на сайт
    """
    _profile: IProfile = inject.attr(IProfile)
    template_name = 'auth_app/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        profile = self._profile.get_profile_by_user_id(self.request.user.pk)
        print(self.request.user.pk)
        return redirect('profile_app:profile', pk=profile.pk)

    def get_success_url(self):
        profile = self._profile.get_profile_by_user_id(self.request.user.pk)
        print(self.request.user.pk)
        return f'/profile/{profile.pk}/'