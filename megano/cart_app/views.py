import inject
from django.views.generic import ListView
from .models import CartItem
from services.calculating_total_amount_cart import CalculatingTotalAmountCart
from .dto import Product, Seller, CartDTO, CartItemDTO


class CartView(ListView):
    """Отображение корзины пользователя"""
    template_name = "cart_app/cart.html"
    context_object_name = 'cart_items'

    def get_queryset(self):
        cart = CartDTO
        cart_items = list()
        if self.request.user.is_authenticated:
            db_cart_items = CartItem.objects.filter(cart=self.request.user.cart)
            for item in db_cart_items:
                product = Product(
                    id=item.product.id,
                    title=item.product.title,
                    description=item.product.description,
                    image=item.product.product_images.first().image.url
                    )
                seller = Seller(
                    id=item.seller.id,
                    name=item.seller.name
                )
                cart.cart_items.append(CartItemDTO(seller=seller, product=product, quantity=item.quantity))
            return cart.cart_items

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.user.is_authenticated:
            context = super().get_context_data(**kwargs)
            total_amount = CalculatingTotalAmountCart(self.request.user.cart)
            context['total_amount'] = total_amount
            return context
