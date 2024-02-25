from abc import ABC, abstractmethod
from catalog.models import Product  # Update the import statement
from typing import List

class ICatalogRepository(ABC):

    @abstractmethod
    def get_products_by_category(self, category_id):
        """Сортировка товаров по категориям."""
        pass

    @abstractmethod
    def get_all_products(self):
        """Все продукты"""
        pass

    @abstractmethod
    def filter_products(self, title: str, price_min: float, price_max: float, available: str,
                        free_delivery: str, seller: List[int], is_limited: str, tag: str, category: List[int]):
        """Фильтр продуктов"""
        pass
