from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from ..models import Profile
from ..forms import UserProfileChangeForm


class UserProfileChangeView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserProfileChangeForm
    template_name = 'profile_app/change_profile.html'

    def get_success_url(self):
        profile_pk = self.object.pk
        messages.success(self.request, 'Профиль успешно обновлен')
        return reverse_lazy('profile_app:change_profile', kwargs={'pk': profile_pk})

    def form_valid(self, form):
        new_username = form.cleaned_data['username']
        if new_username:
            user = self.request.user
            user.username = new_username
            user.save()
        return super().form_valid(form)
