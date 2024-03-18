from abc import abstractmethod, ABC

from django.db.models import QuerySet

from catalog.models import Price, Product
from profile_app.models import Seller


class IPrice(ABC):
    """Интерфейс взаимодействия с данными модели Price"""

    @abstractmethod
    def get_prices_for_calc_total_amount_cart(
            self, products: list[int], sellers: list[int]) -> QuerySet[Price]:
        """Получить экземпляры модели Price связанные с продуктами и продавцами из списков,
        для расчёта общей стоимости корзины"""
        pass
