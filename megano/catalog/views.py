from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Category, Product
from django.http import HttpResponse
from django.views import generic


def catalog_page(request, category_id=None):
    if category_id is not None:
        category = get_object_or_404(Category, pk=category_id)
        cache_key = f'catalog_{category_id}_products'

        products = cache.get(cache_key)

        if not products:
            products = Product.objects.filter(category=category)

            sort_param = request.GET.get('sort')
            if sort_param == 'prices__min':
                products = products.order_by('prices__min')
            elif sort_param == 'prices__max':
                products = products.order_by('-prices__max')

            cache.set(cache_key, products, 86400)

        return render(request, 'catalog/catalog.html', {'category': category, 'products': products})

    all_products = Product.objects.all()
    return render(request, 'catalog/catalog.html', {'category': None, 'products': all_products})


def comparison_page(request):
    return render(request, 'catalog/comparison.html', {})


class ProductDetailViews(generic.DetailView):
    """Представление для отображения детальной страницы товара"""
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"
