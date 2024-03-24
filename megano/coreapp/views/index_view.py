import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
import os
import inject
from coreapp.interfaces.core_interface import ICore
from catalog.interfaces.category_interface import ICategory
from catalog.interfaces.product_interface import IProduct
from discounts_app.interfaces.discounts_interface import IDiscounts
from megano.settings import TIME_OUT_BANNERS


class IndexView(View):

    _BANNERS = 3
    _TOP_PRODUCTS = 8
    _LIMITED_PRODUCTS = 16
    _banner: ICore = inject.attr(ICore)
    _category: ICategory = inject.attr(ICategory)
    _product: IProduct = inject.attr(IProduct)
    _discounts: IDiscounts = inject.attr(IDiscounts)

    def get(self, request) -> HttpResponse:
        """
        Функция формирования контекста для страницы index.html
        _BANNERS = количество баннеров в слайдере на странице.
        Берутся случайные баннеры в количестве _BANNERS из активных на данный момент (is_active=True).
        Выбранные баннеры закешированы на десять минут (параметр берётся из сервиса получения настроек).
        """
        get_banners = self._banner.get_banners()

        if get_banners.count() > 0:
            pks = list(get_banners.values_list('pk', flat=True))
            ln_p = len(pks)
            if self._BANNERS > ln_p:
                self._BANNERS = ln_p
            random_pk = random.sample(pks, k=self._BANNERS)

            context = {"banners": get_banners.filter(pk__in=random_pk),
                       "time_out_banners": TIME_OUT_BANNERS,
                           }
        else:
            context = {"banners": None,
                       "time_out_banners": TIME_OUT_BANNERS,
                       }

        categories= self._category.get_categories_to_display()


        all_lim_products = self._product.get_limited_products()

        pks_products = list(all_lim_products.values_list('pk', flat=True))

        pk_for_1_limited_product = random.choice(pks_products)

        limited_product = all_lim_products.get(pk=pk_for_1_limited_product)
        #Сделать расчет цены и цены со скидкой, таймер

        many_limited_products = all_lim_products.exclude(pk=pk_for_1_limited_product)[:(self._LIMITED_PRODUCTS-1)]
        popular_products = self._product.get_products()[:(self._TOP_PRODUCTS-1)]

        context["categories"] = categories
        context["limited_product"] = limited_product
        context['many_limited_products'] = many_limited_products
        context['popular_products'] = popular_products



        return render(request, "coreapp/index.html", context=context)
