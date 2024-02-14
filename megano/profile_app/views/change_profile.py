from ..models import Profile
from django.views.generic import UpdateView
from ..forms import ProfileForm


class ChangeProfileView(UpdateView):
    model = Profile
    template_name = 'profile_app/change_profile.html'
    # fields = ['phone', 'avatar']
    form_class = ProfileForm
