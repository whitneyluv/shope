import inject
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from catalog.interfaces.catalog_interface import ICatalogRepository
from catalog.forms import ProductFilterForm
from django.views.generic.base import TemplateView
from django.db.models import Q

class CatalogPageView(FormView):
    form_class = ProductFilterForm
    _catalog_repository: ICatalogRepository = inject.attr(ICatalogRepository)

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        category_id = request.GET.get('category_id')
        form = self.form_class(request.GET)  # Create the form instance
        sort_by = request.GET.get('sort_by')

        print(f"Received form data: {request.GET}")  # Print the entire GET parameters

        if form.is_valid():
            title = form.cleaned_data.get('title')
            price_min = form.cleaned_data.get('price_min')
            price_max = form.cleaned_data.get('price_max')
            available = form.cleaned_data.get('available')
            free_delivery = form.cleaned_data.get('free_delivery')
            seller = form.cleaned_data.get('seller')
            is_limited = form.cleaned_data.get('is_limited')
            tag = form.cleaned_data.get('tag')
            category = form.cleaned_data.get('category')

            print(f"Form cleaned_data - title: {title}, price_min: {price_min}, price_max: {price_max}, "
                  f"available: {available}, free_delivery: {free_delivery}, seller: {seller}, "
                  f"is_limited: {is_limited}, tag: {tag}, category: {category}")

            products = self._catalog_repository.filter_products(
                title=title,
                price_min=price_min,
                price_max=price_max,
                available=available,
                free_delivery=free_delivery,
                seller=seller,
                is_limited=is_limited,
                tag=tag,
                category=category
            )

            if sort_by == 'price':
                products = products.order_by('prices__price')

            print(f"Filtered products count: {products.count()}")

            return render(request, self.template_name, {'category': None, 'products': products, 'form': form})

        print("Form is not valid!")
        return render(request, self.template_name, {'category': None, 'form': form})


class ComparisonPageView(TemplateView):
    pass
