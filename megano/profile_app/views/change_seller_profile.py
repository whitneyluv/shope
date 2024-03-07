from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.shortcuts import render
from ..models import Seller
from ..forms import SellerChangeForm


class SellerProfileChangeView(LoginRequiredMixin, UpdateView):
    model = Seller
    form_class = SellerChangeForm
    template_name = 'profile_app/change_seller_profile.html'

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        form = self.form_class(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('profile_app:seller_profile', pk=kwargs['pk'])
        return render(
            request,
            template_name=self.template_name,
            context={
                'message': 'Профиль не был обновлен',
                'seller': instance,
                'form': self.form_class
            }
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile.get(id=self.request.user.id)
        return context
