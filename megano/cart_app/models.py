from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from catalog.models import Product
from coreapp.models.basemodel import BaseModel
from profile_app.models.seller import Seller
from coreapp.choices.cart_status import CART_STATUSES


class Cart(BaseModel):
    """Модель корзины пользователя"""
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="carts",
        verbose_name=_("user")
    )

    status = models.PositiveSmallIntegerField(
        blank=True,
        null=False,
        choices=CART_STATUSES,
        default=1,
        verbose_name=_("status")
    )

    total_amount = models.DecimalField(
        blank=True,
        null=False,
        default=0,
        max_digits=11,
        decimal_places=2,
        verbose_name=_("total amount")
    )

    class Meta:
        db_table = "cart"
        verbose_name = _("cart")
        verbose_name_plural = _("carts")

    def __str__(self):
        return f"Cart user: {self.user}"


class CartItem(BaseModel):
    """Модель товара в корзине пользователя"""
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("cart")
    )

    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        verbose_name=_("seller")
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("product")
    )

    quantity = models.PositiveIntegerField(
        blank=True,
        null=False,
        default=1,
        verbose_name=_("quantity")
    )

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")
