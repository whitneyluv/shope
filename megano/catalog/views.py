import inject
from django.core.cache import cache
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from django.views import generic

from catalog.interfaces.product_interface import IProduct
from catalog.repositories.product_repositories import ProductRepository
from services.add_products_to_cart import AddProductsToCart
from services.add_review import AddReview
from services.recently_viewed_products import RecentlyViewedProductsService
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
    template_name = "catalog/product.html"
    context_object_name = "product"
    show_buy_modal = False
    show_review_modal = False
    __product: IProduct = inject.attr(ProductRepository)

    def get_object(self, *args, **kwargs):
        return self.__product.get_product_for_detail_view(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        """Формирует контекст для шаблона"""
        context = super().get_context_data(**kwargs)
        context['show_buy_modal'] = self.show_buy_modal
        context['show_review_modal'] = self.show_review_modal
        self.show_buy_modal = False
        self.show_review_modal = False
        return context

    def get(self, request: WSGIRequest, *args, **kwargs):
        """Метод обработки GET запросов"""
        if request.user.is_authenticated:
            RecentlyViewedProductsService(user=request.user).add(product_id=kwargs.get('pk'))
        return super().get(request, *args, **kwargs)

    def post(self, request: WSGIRequest, *args, **kwargs):
        """Метод обработки POST запросов"""
        if request.user.is_authenticated:
            if review := request.POST.get('review'):
                self.show_review_modal = True
                AddReview(user=request.user)(
                    product_id=kwargs.get("pk"),
                    review=review
                )
            else:
                self.show_buy_modal = True
                AddProductsToCart(user=request.user)(
                    quantity=int(request.POST.get('num_products')),
                    product_id=kwargs.get("pk"),
                    seller_id=int(request.POST.get('seller_id'))
                )
        return self.get(request, *args, **kwargs)
