from django.urls import reverse
from django.views.generic import CreateView
from ..models import Seller
from ..forms import SellerForm


class SellerCreateView(CreateView):
    template_name = 'profile_app/create_seller_profile.html'
    # model = Seller
    # fields = ['name', 'logo', 'description']
    form_class = SellerForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile_app:seller_profile', kwargs={'pk': self.object.pk})
