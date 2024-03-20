from abc import abstractmethod, ABC
from typing import Optional

from catalog.models import Product


class IProduct(ABC):
    """Интерфейс взаимодействия с данными модели Product"""

    @abstractmethod
    def get_product(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product"""
        pass

    @abstractmethod
    def get_product_for_detail_view(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product с необходимыми связями, агрегациями и аннотациями
        для отображения детальной страницы продукта"""
        pass

    @abstractmethod
    def get_products_for_comparison_list(self, list_pk: list):
        """Получить набор экземпляров модели Product согласно списка list_pk"""
        pass
