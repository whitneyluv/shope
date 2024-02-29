from typing import Dict, Union, List
from django.db.models import Q
from ..models import Product

def filter_products(products: List[Product], filters: Dict[str, Union[str, float, List[int]]]) -> List[Product]:
    title = filters.get('title')
    price_min = filters.get('price_min')
    price_max = filters.get('price_max')
    available = filters.get('available')
    free_delivery = filters.get('free_delivery')
    is_limited = filters.get('is_limited')
    tag = filters.get('tag')
    category = filters.get('category')

    if title:
        products = products.filter(Q(title__icontains=title) | Q(description__icontains=title))

    if price_min is not None:
        products = products.filter(prices__price__gte=float(price_min))

    if price_max is not None and price_max != 'None':
        products = products.filter(prices__price__lte=float(price_max))

    if available != 'Не учитывать':
        products = products.filter(is_active=(available == 'True'))

    if free_delivery != 'Не учитывать':
        products = products.filter(free_delivery=(free_delivery == 'True'))

    if is_limited != 'Не учитывать':
        products = products.filter(is_limited=(is_limited == 'True'))

    if tag:
        products = products.filter(tag__name=tag)

    if category:
        products = products.filter(category__id__in=category)

    return products