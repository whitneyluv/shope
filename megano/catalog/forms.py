from django import forms
from django.db.models import Q
from .models import Seller, Category, Product

class ProductFilterForm(forms.Form):
    title = forms.CharField(label='Название', required=False)
    price_min = forms.DecimalField(label='Цена от', required=False)
    price_max = forms.DecimalField(label='Цена до', required=False)
    available = forms.ChoiceField(choices=[('', 'Не учитывать'), ('True', 'Да'), ('False', 'Нет')],
                                  label='Только товары в наличии', required=False)
    free_delivery = forms.ChoiceField(choices=[('', 'Не учитывать'), ('True', 'Да'), ('False', 'Нет')],
                                      label='С бесплатной доставкой', required=False)
    seller = forms.ModelMultipleChoiceField(queryset=Seller.objects.all(), widget=forms.CheckboxSelectMultiple,
                                            required=False)
    is_limited = forms.ChoiceField(choices=[('', 'Не учитывать'), ('True', 'Да'), ('False', 'Нет')],
                                   label='Ограниченный товар', required=False)
    tag = forms.CharField(label='Тег', required=False)
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple,
                                              required=False)

    def filter_products(self, products):
        if self.cleaned_data['title']:
            title_query = Q(title__icontains=self.cleaned_data['title']) | Q(
                description__icontains=self.cleaned_data['title'])
            products = products.filter(title_query)

        if self.cleaned_data['price_min'] is not None:
            products = products.filter(prices__min__gte=self.cleaned_data['price_min'])

        if self.cleaned_data['price_max'] is not None:
            products = products.filter(prices__max__lte=self.cleaned_data['price_max'])

        if self.cleaned_data['available'] != '':
            products = products.filter(available=self.cleaned_data['available'])

        if self.cleaned_data['free_delivery'] != '':
            products = products.filter(free_delivery=self.cleaned_data['free_delivery'])

        if self.cleaned_data['seller']:
            products = products.filter(seller__in=self.cleaned_data['seller'])

        if self.cleaned_data['is_limited'] != '':
            products = products.filter(is_limited=self.cleaned_data['is_limited'])

        if self.cleaned_data['tag']:
            products = products.filter(tag__name__icontains=self.cleaned_data['tag'])

        if self.cleaned_data['category']:
            products = products.filter(category__in=self.cleaned_data['category'])

        return products