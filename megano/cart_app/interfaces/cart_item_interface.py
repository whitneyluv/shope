from abc import abstractmethod, ABC

from django.db.models import QuerySet

from cart_app.models import CartItem, Cart


class ICartItem(ABC):
    """Интерфейс взаимодействия с данными модели CartItem"""

    @abstractmethod
    def save(self, model: CartItem) -> None:
        """Сохранить экземпляр модели CartItem"""
        pass

    @abstractmethod
    def get_items_for_calc_total_amount_cart(self, cart: Cart) -> QuerySet[CartItem]:
        """Получить экземпляры модели CartItem связанные с корзиной cart,
        для расчёта общей стоимости корзины"""
        pass

    @abstractmethod
    def get_all_items_in_cart(self, cart: Cart) -> QuerySet[CartItem]:
        """Получить экземпляры модели CartItem связанные с корзиной cart
        """
        pass
