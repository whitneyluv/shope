from random import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Banner
import os


def base_view(request: HttpRequest) -> HttpResponse:
    return render(request, "coreapp/base.html")


def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "coreapp/about.html")


class IndexView(View):

    _BANNERS = 3

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Функция формирования контекста для страницы index.html
        q_banners = количество баннеров в слайдере на странице.
        Берутся случайные баннеры в количестве q_banners из активных на данный момент (is_active=True).
        Выбранные баннеры закешированы на десять минут (параметр берётся из сервиса получения настроек).
        """

        pks = list(Banner.objects.all().filter(is_active=True).values_list('pk', flat=True))
        if self._BANNERS > len(pks):
            self._BANNERS = len(pks)
        random_pk = random.sample(pks, k=self._BANNERS)

        context = {"banners": Banner.objects.all().filter(pk__in=random_pk),
                   "time_out_banners": os.getenv("TIME_OUT_BANNERS"),
                   }

        return render(request, "coreapp/index.html", context=context)
