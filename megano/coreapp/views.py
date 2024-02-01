from random import random
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Banner


def base_view(request: HttpRequest) -> HttpResponse:
    return render(request, "coreapp/base.html")


def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "coreapp/about.html")


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Функция формирования контекста для страницы index.html
        q_banners = количество баннеров в слайдере на странице.
        Берутся случайные баннеры в количестве q_banners из активных на данный момент (is_active=True).
        Выбранные баннеры закешированы на десять минут (параметр берётся из сервиса получения настроек).
        """
        q_banners = 3

        pks = list(Banner.objects.all().filter(is_active=True).values_list('pk', flat=True))
        if q_banners > len(pks):
            q_banners = len(pks)
        random_pk = random.sample(pks, k=q_banners)

        context = {"banners": Banner.objects.all().filter(pk__in=random_pk),
                   "time_out_banners": 600,   # будем брать данные из админки
                   }

        return render(request, "coreapp/index.html", context=context)
