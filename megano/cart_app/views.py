import inject
from django.views.generic import ListView
from .interfaces.cart_item_interface import ICartItem
from services.dto_calculating_total_amount_cart import DTOCalculatingTotalAmountCart
from .dto import Product, Seller, CartDTO, CartItemDTO


class CartView(ListView):
    """Отображение корзины пользователя"""
    template_name = "cart_app/cart.html"
    context_object_name = 'cart'
    _cart_items: ICartItem = inject.attr(ICartItem)

    def get_queryset(self):
        cart_items = list()
        if self.request.user.is_authenticated:
            for item in self._cart_items.get_all_items_in_cart(self.request.user.cart):
                product = Product().authenticated_user_init(item.product)
                seller = Seller().authenticated_user_init(item.seller)
                cart_items.append(CartItemDTO(seller=seller, product=product, quantity=item.quantity))
        else:
            for item in self.request.session.get('cart'):
                product = Product().session_init(item['product_id'])
                seller = Seller().session_init(item['seller_id'])
                cart_items.append(CartItemDTO(seller=seller, product=product, quantity=item['num_products']))
        return CartDTO(cart_items=cart_items, total_amount=DTOCalculatingTotalAmountCart(cart_items)())
