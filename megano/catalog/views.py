from django.core.cache import cache
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Min
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Category, Product


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

        return render(request, 'catalog/catalog.html',
                      {'category': category, 'products': products})

    all_products = Product.objects.all()
    return render(request, 'catalog/catalog.html', {'category': None, 'products': all_products})


def comparison_page(request):
    return render(request, 'catalog/comparison.html', {})


class ProductDetailViews(generic.DetailView):
    """Представление для отображения детальной страницы товара"""
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"
    show_modal = False

    def get_queryset(self):
        """Формирует запрос для получения объекта Product"""
        return Product.objects.annotate(
            min_price=Min('prices__price')).prefetch_related(
            'prices', 'product_characteristics', 'product_images')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_modal'] = self.show_modal
        self.show_modal = False
        return context

    def get(self, request: WSGIRequest, *args, **kwargs):
        """Метод обработки GET запросов"""
        product_id = kwargs.get('pk')
        # TODO добавить вызов метода добавления товара в список просмотренных когда появится
        return super().get(request, *args, **kwargs)

    def post(self, request: WSGIRequest, *args, **kwargs):
        """Метод обработки POST запросов"""
        self.show_modal = True
        num_products = int(request.POST.get('num_products'))
        # TODO добавить вызов метода добавления товара в корзину когда появится
        return self.get(request, *args, **kwargs)
