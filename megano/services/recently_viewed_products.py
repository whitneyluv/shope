from django.contrib.auth import get_user_model
from catalog.models import Product, RecentlyViewedProducts


class RecentlyViewedProductsService:
    """Класс для реализации методов работы с недавно просмотренными товарами"""

    def __init__(self, user_id: int) -> None:
        self.user = get_user_model().objects.get(id=user_id)

    def add(self, product_id: int) -> None:
        """Метод добавления продукта в список недавно просмотренных или обновления поля updated_at
        модели RecentlyViewedProducts если данный продукт ранее просматривался пользователем"""
        product = Product.objects.get(id=product_id)
        if view := RecentlyViewedProducts.objects.filter(user=self.user, product=product).first():
            view.save()
        else:
            RecentlyViewedProducts(
                user=self.user,
                product=product
            ).save()
