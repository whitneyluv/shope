from ..models import Seller
from django.views.generic import DetailView


class SellerProfileView(DetailView):
    template_name = 'profile_app/seller_profile.html'
    model = Seller
    context_object_name = 'seller'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.request.user.profile.get(id=self.request.user.id)
        return context
