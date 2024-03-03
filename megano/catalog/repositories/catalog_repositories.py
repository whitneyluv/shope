from django.db.models import Q, Min
from typing import Union, Dict
from django.db.models import QuerySet
import inject
from beartype import beartype
from catalog.interfaces.catalog_interface import ICatalogRepository
from ..models import Product
from ..utils.filter_utils import filter_products

class CatalogRepository(ICatalogRepository):

    @beartype
    def get_products_by_category(self, category_id: int) -> QuerySet[Product]:
        if category_id is not None:
            return Product.objects.filter(category__id=category_id)
        return Product.objects.all()

    @beartype
    def get_all_products(self) -> QuerySet[Product]:
        return Product.objects.all()

    @beartype
    def filter_products(self, **filters) -> QuerySet[Product]:
        print(f"Before filtering - filters: {filters}")

        products = self.get_all_products()

        products = filter_products(products, filters)

        print(f"Filtered products count: {products.count()}")

        return products
