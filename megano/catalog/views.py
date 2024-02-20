from django.core.cache import cache
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Min, F
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Category, Product
from services.add_products_to_cart import AddProductsToCart
from services.recently_viewed_products import RecentlyViewedProducts


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
            min_price=Min('prices__price')).filter(
            prices__price=F('min_price')).annotate(
            min_price_seller_id=F('prices__seller')).prefetch_related(
            'prices', 'product_characteristics', 'product_images')

    def get_context_data(self, **kwargs):
        """Формирует контекст для шаблона"""
        context = super().get_context_data(**kwargs)
        context['show_modal'] = self.show_modal
        self.show_modal = False
        return context

    def get(self, request: WSGIRequest, *args, **kwargs):
        """Метод обработки GET запросов"""
        RecentlyViewedProducts(user_id=request.user.pk).add(product_id=kwargs.get('pk'))
        return super().get(request, *args, **kwargs)

    def post(self, request: WSGIRequest, *args, **kwargs):
        """Метод обработки POST запросов"""
        self.show_modal = True
        AddProductsToCart(user_id=request.user.pk)(
            quantity=int(request.POST.get('num_products')),
            product_id=kwargs.get("pk"),
            seller_id=int(request.POST.get('seller_id'))
        )
        return self.get(request, *args, **kwargs)
