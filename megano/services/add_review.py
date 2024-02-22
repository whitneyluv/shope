from django.contrib.auth import get_user_model

from catalog.models import Review, Product


class AddReview:
    """Класс для реализации методов добавления отзывов к продукту"""

    def __call__(self, product_id: int, user_id: int, review: str) -> None:
        """Метод добавления отзыва к продукту"""
        Review(
            product=Product.objects.get(id=product_id),
            author=get_user_model().objects.get(id=user_id),
            review=review
        ).save()
