from ..models import Profile
from django.views.generic import View, DetailView


class ProfileView(DetailView):
    template_name = 'profile_app/profile.html'
    model = Profile
    context_object_name = 'profile'
