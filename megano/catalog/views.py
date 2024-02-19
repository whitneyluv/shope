from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from django.views import View
from .models import Category, Product
from .forms import ProductFilterForm
from .repositories import ProductRepository

class CatalogPageView(View):
    template_name = 'catalog/catalog.html'

    def get(self, request, category_id=None):
        filter_form = ProductFilterForm(request.GET)
        category = None

        if category_id is not None:
            category = get_object_or_404(Category, pk=category_id)
            cache_key = f'catalog_{category_id}_products'

            products_in_category = cache.get(cache_key)
            if not products_in_category:
                products_in_category = ProductRepository.get_products_by_category(category)

                sort_param = request.GET.get('sort')
                if sort_param:
                    products_in_category = ProductRepository.get_products_by_category(category, sort_param)

                cache.set(cache_key, products_in_category, 86400)

            products = products_in_category
        else:
            products = Product.objects.all().prefetch_related('prices')

        if filter_form.is_valid():
            price_min = None
            price_max = None

            if 'price_min' in request.GET:
                price_min = float(request.GET['price_min'])

            if 'price_max' in request.GET:
                price_max = float(request.GET['price_max'])

            products = ProductRepository.filter_products(products, filter_form, price_min, price_max)
        else:
            print("Form is not valid. Errors:", filter_form.errors)

        return render(request, self.template_name,
                      {'category': category, 'products': products, 'filter_form': filter_form})


class ComparisonPageView(View):
    template_name = 'catalog/comparison.html'

    def get(self, request):
        return render(request, self.template_name, context={})