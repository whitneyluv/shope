from django.db import models
from django.contrib.auth import get_user_model
from coreapp.choices.cart_status import CART_STATUSES
from coreapp.models import BaseModel
from catalog.models import Product
from profile_app.models.seller import Seller


class Cart(BaseModel):
    """Модель корзины пользователя"""
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="carts",
        verbose_name="пользователь"
    )

    status = models.PositiveSmallIntegerField(
        blank=True,
        null=False,
        choices=CART_STATUSES,
        default=1,
        verbose_name="статус"
    )

    total_amount = models.DecimalField(
        blank=True,
        null=False,
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name="общая стоимость"
    )

    class Meta:
        db_table = "cart"
        verbose_name = "корзина"
        verbose_name_plural = "корзины"

    def __str__(self):
        return f"Cart user: {self.user}"


class CartItem(BaseModel):
    """Модель товара в корзине пользователя"""
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="корзина"
    )

    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        verbose_name="продавец"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="товар"
    )

    quantity = models.PositiveIntegerField(
        blank=True,
        null=False,
        default=1,
        verbose_name="количество"
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"
