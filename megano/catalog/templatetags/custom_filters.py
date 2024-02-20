from decimal import Decimal

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def price_format(value):
    """Разделяет пробелами разряды цены, ограничивает двумя знаками
    после запятой и добавляет символ валюты"""
    value = Decimal(value).quantize(Decimal('.00'))
    return f'{value:,} {settings.CURRENCY_SYMBOL}'.replace(',', ' ')
