from typing import Optional
from beartype import beartype
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Min, F
from catalog.interfaces.product_interface import IProduct
from catalog.models import Product


class ProductRepository(IProduct):
    """Для реализации методов взаимодействия с данными
    модели Product на основании интерфейса IProduct"""

    @beartype
    def get_product(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product"""
        try:
            return Product.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_product_with_image(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product с изображениями"""
        try:
            return Product.objects.get(pk=pk).select_related('product_image')
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_product_for_detail_view(self, pk: int) -> Optional[Product]:
        """Получить экземпляр модели Product с необходимыми связями и аннотациями
        для отображения детальной страницы товара"""
        try:
            return Product.objects.annotate(
                min_price=Min('prices__price')).filter(
                prices__price=F('min_price')).annotate(
                min_price_seller_id=F('prices__seller')).prefetch_related(
                'prices', 'product_characteristics', 'product_images', 'reviews').get(pk=pk)
        except ObjectDoesNotExist:
            return None
