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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

            page = request.GET.get('page', 1)
            paginator = Paginator(products, 10)
            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)

            context = {'category': None, 'products': products, 'form': form}
            return render(request, self.template_name, context)

        return render(request, self.template_name, {'category': None, 'form': form})

class ComparisonPageView(TemplateView):


    def get(self, request, *args, **kwargs):
        return render(request, 'catalog/comparison.html', {})
