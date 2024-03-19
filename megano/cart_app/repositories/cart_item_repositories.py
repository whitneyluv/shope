from beartype import beartype

from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.models import CartItem, Cart
from django.db.models import QuerySet


class CartItemRepository(ICartItem):
    """Для реализации методов взаимодействия с данными
    модели CartItem на основании интерфейса ICartItem"""

    @beartype
    def save(self, model: CartItem) -> None:
        """Сохранить экземпляр модели CartItem"""
        model.save()

    @beartype
    def get_items_for_calc_total_amount_cart(self, cart: Cart) -> QuerySet[CartItem]:
        """Получить экземпляры модели CartItem связанные с корзиной cart,
        для расчёта общей стоимости корзины"""
        return CartItem.objects.filter(cart=cart).all().select_related('product', 'seller')

    @beartype
    def get_all_items_in_cart(self, cart: Cart) -> QuerySet[CartItem]:
        """
        Получить экземпляры модели CartItem связанные с корзиной cart
        """
        return CartItem.objects.filter(cart=cart)

    @beartype
    def sum_all_items_in_cart(self, cart: Cart) -> int:
        """Получить количество товаров в корзине
        """
        return sum([item.quantity for item in CartItem.objects.filter(cart=cart)])
