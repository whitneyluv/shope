from profile_app.models import Profile
from django.views.generic import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied


class ProfileView(UserPassesTestMixin, DetailView):

    def ban_viewing_another_profiles(self):
        if self.request.resolver_match.kwargs['pk'] != self.request.user.profile.pk:
            raise PermissionDenied
        return True

    def get_test_func(self):
        return self.ban_viewing_another_profiles

    template_name = 'profile_app/profile.html'
    model = Profile
    context_object_name = 'profile'
