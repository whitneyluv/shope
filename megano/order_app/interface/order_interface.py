from abc import abstractmethod
from order_app.models.order import Order
from cart_app.models import CartItem


class IOrder:

    @abstractmethod
    def save(self, model: Order):
        """Сохранить экземпляр модели Order"""
        pass

    @abstractmethod
    def get_order_by_pk(self, pk):
        """Получить заказ по ключу (pk)"""
        pass

    @abstractmethod
    def get_order_items(self, order_pk):
        """Получить экземпляры модели OrderItems по конкретному заказу"""
        pass

    @abstractmethod
    def get_all_users_orders(self, user_pk):
        """Получить все заказы юзер"""
        pass

    @abstractmethod
    def get_all_orders(self):
        """Получить все заказы"""
        pass

    @abstractmethod
    def get_cart_items(self, user_pk):
        """Получить все экземпляры CartItem из корзины пользователя"""
        pass

    @abstractmethod
    def delete_cart_item_from_cart(self, model: CartItem):
        """Удаление элемента CartItem из корзины"""
        pass
