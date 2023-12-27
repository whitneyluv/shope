from django.db import models
from django.contrib.auth import get_user_model


class Cart(models.Model):
    """Модель корзины пользователя"""
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="carts",
        verbose_name="пользователь"
    )

    class Meta:
        db_table = "cart"
        verbose_name = "корзина"
        verbose_name_plural = "корзины"

    def __str__(self):
        return f"Cart user: {self.user}"


class ProductCart(models.Model):
    """Модель товара в корзине пользователя"""
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="корзина"
    )
    # TODO добавить поле когда появится модель
    # product = models.ForeignKey("ProductShop", on_delete=models.CASCADE, verbose_name="товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="количество")
    added_date = models.DateField(auto_now_add=True, verbose_name="дата добавления")

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
