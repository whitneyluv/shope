from beartype import beartype
from django.core.exceptions import ObjectDoesNotExist

from profile_app.interfaces.seller_interface import ISeller
from profile_app.models.seller import Seller


class SellerRepository(ISeller):
    """Для реализации методов взаимодействия с данными
    модели Seller на основании интерфейса ISeller"""

    @beartype
    def get_seller(self, pk: int) -> Seller | None:
        """Получить экземпляр модели Product"""
        try:
            return Seller.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None
