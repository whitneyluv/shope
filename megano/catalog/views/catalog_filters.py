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

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        category_id = request.GET.get('category_id')
        form = self.form_class(request.GET)
        sort_by = request.GET.get('sort_by')

        if form.is_valid():
            products = self._catalog_repository.filter_products(**form.cleaned_data)

            products = filter_products(products, form.cleaned_data)

            if sort_by == 'price':
                products = products.order_by('prices__price')

            context = {'category': None, 'products': products, 'form': form}
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'category': None, 'form': form})

class ComparisonPageView(TemplateView):
    pass
