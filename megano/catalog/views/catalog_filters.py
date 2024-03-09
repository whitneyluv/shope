from django.shortcuts import render
import inject
from django.views.generic import ListView, TemplateView
from django.db.models import Min  # Добавлен импорт для функции Min
from ..interfaces.catalog_interface import ICatalogRepository
from catalog.utils.filter_utils import filter_products
from catalog.models import Product, Seller, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CatalogPageView(ListView):
    template_name = 'catalog/catalog'
    _catalog_repository: ICatalogRepository = inject.attr(ICatalogRepository)
    paginate_by = 9

    def get_queryset(self):
        return self._get_filtered_and_sorted_products()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = self._get_filtered_and_sorted_products()
        context['products'] = products

        paginator = Paginator(products, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            products_page = paginator.page(page)
        except PageNotAnInteger:
            products_page = paginator.page(1)
        except EmptyPage:
            products_page = paginator.page(paginator.num_pages)

        context['products_page'] = products_page
        return context

    def _get_filtered_and_sorted_products(self):
        try:
            filters = {
                'category_id': self.request.GET.get('category_id'),
                'title': self.request.GET.get('title'),
                'available': self.request.GET.get('available'),
                'free_delivery': self.request.GET.get('free_delivery'),
                'is_limited': self.request.GET.get('is_limited'),
                'tag': self.request.GET.get('tag'),
                'category': self.request.GET.getlist('category'),
            }

            price_range = self.request.GET.get('price')
            if price_range:
                price_min, price_max = map(float, price_range.split(';'))
                filters['price_min'] = price_min
                filters['price_max'] = price_max

            products = self._catalog_repository.filter_products(**filters)

            sort = self.request.GET.get('sort')
            if sort == 'price':
                sort_direction = self.request.GET.get('sort_direction', 'asc')

                sort_field = f'prices__price__min{"-" if sort_direction == "desc" else ""}'
                products = products.annotate(prices__price__min=Min('prices__price')).order_by(sort_field)
            elif sort == 'popularity':
                products = products.order_by('-popularity')
            elif sort == 'created_at':
                products = products.order_by('-created_at')

            return products
        except KeyError:
            return Product.objects.none()

    def get(self, request, **kwargs):
        return super().get(request, **kwargs)


class ComparisonPageView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'catalog/comparison.html', {})
