from beartype import beartype

from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.models import CartItem


class CartItemRepository(ICartItem):
    """Для реализации методов взаимодействия с данными
    модели CartItem на основании интерфейса ICartItem"""

    @beartype
    def save(self, model: CartItem) -> None:
        """Сохранить экземпляр модели CartItem"""
        model.save()
