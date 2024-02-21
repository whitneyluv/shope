from django.db.models import Q, Min, Max
from .models import Product

class ProductRepository:
    @staticmethod
    def get_products_by_category(category, sort_param=None):
        products = Product.objects.filter(category=category).prefetch_related('prices')

        if sort_param == 'price_min':
            products = products.annotate(min_price=Min('prices__price')).order_by('min_price')
        elif sort_param == 'price_max':
            products = products.annotate(max_price=Max('prices__price')).order_by('-max_price')

        return products

    @staticmethod
    def filter_products(products, filter_form, price_min=None, price_max=None):
        query = Q()

        if filter_form.cleaned_data.get('title'):
            query &= (Q(title__icontains=filter_form.cleaned_data['title']) |
                      Q(description__icontains=filter_form.cleaned_data['title']))

        if price_min is not None and price_max is not None:
            query &= Q(prices__price__gte=price_min) & Q(prices__price__lte=price_max)

        if filter_form.cleaned_data.get('available') == 'True':
            query &= Q(prices__seller__available=True)
        elif filter_form.cleaned_data.get('available') == 'False':
            query &= Q(prices__seller__available=False)

        if filter_form.cleaned_data.get('free_delivery') == 'True':
            query &= Q(prices__seller__free_delivery=True)
        elif filter_form.cleaned_data.get('free_delivery') == 'False':
            query &= Q(prices__seller__free_delivery=False)

        seller_conditions = (
            Q(prices__seller__in=filter_form.cleaned_data['seller'])
            if filter_form.cleaned_data.get('seller') else Q()
        )
        query &= seller_conditions

        if filter_form.cleaned_data.get('is_limited') == 'True':
            query &= Q(is_limited=True)
        elif filter_form.cleaned_data.get('is_limited') == 'False':
            query &= Q(is_limited=False)

        if filter_form.cleaned_data.get('tag'):
            tags = filter_form.cleaned_data['tag'].split(',')
            query &= Q(tag__name__in=tags)

        category_conditions = (
            Q(category__in=filter_form.cleaned_data['category'])
            if filter_form.cleaned_data.get('category') else Q()
        )
        query &= category_conditions

        return products.filter(query).distinct()

    @staticmethod
    def filter_products_with_price_range(products, filter_form, price_min=None, price_max=None):
        return ProductRepository.filter_products(products, filter_form, price_min, price_max)