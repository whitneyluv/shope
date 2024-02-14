from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from profile_app.models import Profile

class UserLoginView(LoginView):
    """
    View функция отображения страницы логирования на сайт
    """
    template_name = 'auth_app/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        profile = Profile.objects.get(user_id=self.request.user.pk)
        return redirect('profile_app:profile', pk=profile.pk)

    def get_success_url(self):
        profile = Profile.objects.get(user_id=self.request.user.pk)
        return f'/profile/{profile.pk}/'

