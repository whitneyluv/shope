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
    def get_product_with_image(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product с изображениями"""
        pass

    @abstractmethod
    def get_product_for_detail_view(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product с необходимыми связями, агрегациями и аннотациями
        для отображения детальной страницы продукта"""
        pass
