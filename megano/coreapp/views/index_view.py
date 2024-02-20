from random import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from coreapp.models.banner import Banner
import os
import inject
from coreapp.interfaces.core_interface import ICore


class IndexView(View):

    _BANNERS = 3
    _banner: ICore = inject.attr(ICore)

    def get(self, request) -> HttpResponse:
        """
        Функция формирования контекста для страницы index.html
        _BANNERS = количество баннеров в слайдере на странице.
        Берутся случайные баннеры в количестве _BANNERS из активных на данный момент (is_active=True).
        Выбранные баннеры закешированы на десять минут (параметр берётся из сервиса получения настроек).
        """
        get_banners = self._banner.get_banners(self.request)
        pks = list(get_banners.values_list('pk', flat=True))
        ln_p = len(pks)
        if self._BANNERS > ln_p:
            self._BANNERS = ln_p
        random_pk = random.sample(pks, k=self._BANNERS)

        context = {"banners": get_banners.filter(pk__in=random_pk),
                   "time_out_banners": os.getenv("TIME_OUT_BANNERS"),
                   }

        return render(request, "coreapp/index.html", context=context)
