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
    def get_all_users_orders(self, user_pk):
        """Получить все заказы юзер"""
        pass

    @abstractmethod
    def get_all_orders(self):
        """Получить все заказы"""
        pass

