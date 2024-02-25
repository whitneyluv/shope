from django.db.models import Q, Min
from typing import List, Union
import inject
from catalog.interfaces.catalog_interface import ICatalogRepository
from ..models import Product

class CatalogRepository(ICatalogRepository):

    def get_products_by_category(self, category_id: int) -> List[Product]:
        if category_id is not None:
            return Product.objects.filter(category__id=category_id)
        return Product.objects.all()

    def get_all_products(self) -> List[Product]:
        return Product.objects.all()

    def filter_products(self, title: str = None, price_min: Union[float, str] = None,
                        price_max: Union[float, str] = None,
                        available: str = None, free_delivery: str = None,
                        seller: List[int] = None, is_limited: str = None, tag: str = None,
                        category: List[int] = None, sort_by: str = None) -> List[Product]:

        print(f"Before filtering - title: {title}, price_min: {price_min}, price_max: {price_max}, "
              f"available: {available}, free_delivery: {free_delivery}, seller: {seller}, "
              f"is_limited: {is_limited}, tag: {tag}, category: {category}, sort_by: {sort_by}")

        products = self.get_all_products()

        if title:
            products = products.filter(Q(title__icontains=title) | Q(description__icontains=title))

        print(f"After title filter - products count: {products.count()}")

        if price_min is not None:
            products = products.filter(prices__price__gte=price_min)

        print(f"After price_min filter - products count: {products.count()}")

        if price_max is not None:
            products = products.filter(prices__price__lte=price_max)

        print(f"After price_max filter - products count: {products.count()}")

        if available != 'Не учитывать':
            products = products.filter(is_active=(available == 'True'))

        print(f"After available filter - products count: {products.count()}")

        if free_delivery != 'Не учитывать':
            products = products.filter(free_delivery=(free_delivery == 'True'))

        print(f"After free_delivery filter - products count: {products.count()}")

        if seller:
            unique_seller_ids = set()
            for product in products:
                unique_seller_ids.update(product.prices.values_list('seller_id', flat=True))

            products = products.filter(prices__seller__id__in=unique_seller_ids)

        print(f"After seller filter - products count: {products.count()}")

        if is_limited != 'Не учитывать':
            products = products.filter(is_limited=(is_limited == 'True'))

        print(f"After is_limited filter - products count: {products.count()}")

        if tag:
            products = products.filter(tag__name=tag)

        print(f"After tag filter - products count: {products.count()}")

        if category:
            products = products.filter(category__id__in=category)

        print(f"After category filter - products count: {products.count()}")

        if sort_by:
            if sort_by == 'price':
                products = products.annotate(min_price=Min('prices__price')).order_by('min_price')

        print(f"Filtered products count: {products.count()}")

        return products
