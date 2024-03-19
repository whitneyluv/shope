import inject
from django.shortcuts import redirect
from ..interfaces.cart_item_interface import ICartItem
from cart_app.models import CartItem
_cart_item: ICartItem = inject.attr(ICartItem)


def remove_cart_items(request):
    """
    Функция удаления продукта из корзины
    """
    data = request.GET
    if request.user.is_authenticated:
        CartItem.objects.get(product__id=data['product_id'], seller__id=data['seller_id']).delete()
        # _cart_item.delete(product_id=data['product_id'], seller_id=data['seller_id'])
    return redirect('cart:cart')
