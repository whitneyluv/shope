from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from .models import Category, Product, Seller
from .forms import ProductFilterForm

def catalog_page(request, category_id=None):
    category = None

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

        filter_form = ProductFilterForm(request.GET)

        if filter_form.is_valid():
            products = filter_form.filter_products(products)
        else:
            print("Форма фильтра не допустима. Ошибки:", filter_form.errors)

        return render(request, 'catalog/catalog.html', {'category': category, 'products': products, 'filter_form': filter_form})

    all_products = Product.objects.all()
    filter_form = ProductFilterForm(request.GET)

    if filter_form.is_valid():
        print("Форма фильтра допустима. Данные:", filter_form.cleaned_data)
        all_products = filter_form.filter_products(all_products)
    else:
        print("Форма фильтра не допустима. Ошибки:", filter_form.errors)

    return render(request, 'catalog/catalog.html', {'category': category, 'products': all_products, 'filter_form': filter_form})

def comparison_page(request):
    return render(request, 'catalog/comparison.html', {})
