from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from catalog.models import Product, Price
from coreapp.choices.cart_status import CART_STATUSES
from coreapp.models.basemodel import BaseModel
from profile_app.models.seller import Seller


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

    @property
    def total_amount(self):
        """Динамический расчёт общей стоимости корзины по актуальной цене продукта"""
        total = Decimal("0.00")
        products = []
        sellers = []

        items = CartItem.objects.filter(cart=self).all().select_related('product', 'seller')
        [(products.append(item.product), sellers.append(item.seller)) for item in items]

        prices = Price.objects.filter(
            product__in=products,
            seller__in=sellers
        ).select_related('product', 'seller')

        prices_dict = {(price.product.pk, price.seller.pk): price for price in prices}

        for item in items:
            price = prices_dict.get((item.product.pk, item.seller.pk))
            total += item.quantity * price.price if price else 0
        return total

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
