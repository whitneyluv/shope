from django.contrib.auth import get_user_model


class RecentlyViewedProducts:
    """Класс для реализации методов работы с недавно просмотренными товарами"""

    def __init__(self, user_id: int) -> None:
        self.user = get_user_model().objects.get(id=user_id)

    def add(self, product_id: int) -> None:
        """Метод добавления товара в список недавно просмотренных"""
        ...
