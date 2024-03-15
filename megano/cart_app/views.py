import inject
from django.views.generic import ListView
from .models import CartItem, Cart
from catalog.interfaces import IProduct
from profile_app.interfaces import ISeller
from services.calculating_total_amount_cart import CalculatingTotalAmountCart
from auth_app.models import User


class CartView(ListView):
    """Отображение корзины пользователя"""
    template_name = "cart_app/cart.html"
    context_object_name = 'cart_items'
    _product: IProduct = inject.attr(IProduct)
    _seller: ISeller = inject.attr(ISeller)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            cart_items = CartItem.objects.filter(cart=self.request.user.cart)
            return cart_items
        else:
            user = User.objects.get(pk=1)
            cart = Cart.objects.get(user=user)
            cart_items = []


    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            total_amount = CalculatingTotalAmountCart(self.request.user.cart)
            context['total_amount'] = total_amount
            return context

