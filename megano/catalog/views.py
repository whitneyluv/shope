from django import forms
from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from .models import Category, Product, Seller

class ProductFilterForm(forms.Form):
    title = forms.CharField(label='Название', required=False)
    price_min = forms.DecimalField(label='Цена от', required=False)
    price_max = forms.DecimalField(label='Цена до', required=False)
    available = forms.BooleanField(label='Только товары в наличии', required=False)
    free_delivery = forms.BooleanField(label='С бесплатной доставкой', required=False)
    seller = forms.ModelMultipleChoiceField(queryset=Seller.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)

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

        filter_form = ProductFilterForm(request.GET)

        if filter_form.is_valid():
            if filter_form.cleaned_data['title']:
                products = products.filter(title__icontains=filter_form.cleaned_data['title'])

            if filter_form.cleaned_data['price_min']:
                products = products.filter(prices__min__gte=filter_form.cleaned_data['price_min'])

            if filter_form.cleaned_data['price_max']:
                products = products.filter(prices__max__lte=filter_form.cleaned_data['price_max'])

            if filter_form.cleaned_data['available']:
                products = products.filter(available=True)

            if filter_form.cleaned_data['free_delivery']:
                products = products.filter(free_delivery=True)

            if filter_form.cleaned_data['seller']:
                products = products.filter(seller__in=filter_form.cleaned_data['seller'])

        else:
            print("Filter form is not valid. Errors:", filter_form.errors)

        return render(request, 'catalog/catalog.html', {'category': category, 'products': products, 'filter_form': filter_form})

    all_products = Product.objects.all()
    filter_form = ProductFilterForm(request.GET)

    if filter_form.is_valid():
        if filter_form.cleaned_data['title']:
            all_products = all_products.filter(title__icontains=filter_form.cleaned_data['title'])

        if filter_form.cleaned_data['price_min']:
            all_products = all_products.filter(prices__min__gte=filter_form.cleaned_data['price_min'])

        if filter_form.cleaned_data['price_max']:
            all_products = all_products.filter(prices__max__lte=filter_form.cleaned_data['price_max'])

        if filter_form.cleaned_data['available']:
            all_products = all_products.filter(available=True)

        if filter_form.cleaned_data['free_delivery']:
            all_products = all_products.filter(free_delivery=True)

        if filter_form.cleaned_data['seller']:
            all_products = all_products.filter(seller__in=filter_form.cleaned_data['seller'])

    else:
        print("Filter form is not valid. Errors:", filter_form.errors)

    return render(request, 'catalog/catalog.html', {'category': None, 'products': all_products, 'filter_form': filter_form})

def comparison_page(request):
    return render(request, 'catalog/comparison.html', {})
