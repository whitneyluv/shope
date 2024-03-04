from django.shortcuts import render
import inject
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from ..interfaces.catalog_interface import ICatalogRepository
from catalog.forms import ProductFilterForm
from django.views.generic.base import TemplateView
from django.db.models import Q
from catalog.utils.filter_utils import filter_products
from catalog.models import Product, Category, Price

class CatalogPageView(FormView):
    form_class = ProductFilterForm
    _catalog_repository: ICatalogRepository = inject.attr(ICatalogRepository)
    template_name = 'catalog/catalog.html'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        form = self.get_form()
        sort = request.GET.get('sort', 'popularity')

        if form.is_valid():
            products = self._catalog_repository.filter_products(**form.cleaned_data)

            if sort == 'price':
                products = products.order_by('prices__price')
                if request.GET.get('sort_direction') == 'desc':
                    products = products.reverse()

            context = {'category': None, 'products': products, 'form': form}
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'category': None, 'form': form})

class ComparisonPageView(TemplateView):
    pass
