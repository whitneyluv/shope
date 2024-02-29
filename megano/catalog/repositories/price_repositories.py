from beartype import beartype
from django.db.models import QuerySet

from catalog.interfaces.price_interface import IPrice
from catalog.models import Price, Product
from profile_app.models import Seller


class PriceRepository(IPrice):
    """Для реализации методов взаимодействия с данными
    модели Price на основании интерфейса IPrice"""

    @beartype
    def get_prices_for_calc_total_amount_cart(
            self, products: list[Product], sellers: list[Seller]) -> QuerySet[Price]:
        """Получить экземпляры модели Price связанные с продуктами и продавцами из списков,
        для расчёта общей стоимости корзины"""
        return Price.objects.filter(
            product__in=products,
            seller__in=sellers
        ).select_related('product', 'seller')
