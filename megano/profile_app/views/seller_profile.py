from ..models import Seller
from django.views.generic import DetailView


class SellerProfileView(DetailView):
    template_name = 'profile_app/seller_profile.html'
    model = Seller
    context_object_name = 'seller'
