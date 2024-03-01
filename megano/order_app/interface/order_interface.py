from abc import abstractmethod
from megano.order_app.models.order import Order


class IOrder:

    @abstractmethod
    def save(self, model: Order):
        """Сохранить экземпляр модели Order"""
        pass

    @abstractmethod
    def get_order_by_pk(self, pk):
        """Получить заказ по ключу (pk)"""
        pass
