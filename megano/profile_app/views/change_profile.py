from ..models import Profile
from django.views.generic import UpdateView
from ..forms import ProfileChangeForm


class ChangeProfileView(UpdateView):
    model = Profile
    template_name = 'profile_app/change_profile.html'
    form_class = ProfileChangeForm
