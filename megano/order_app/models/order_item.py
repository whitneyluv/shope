from django.db import models
from megano.profile_app.models.seller import Seller
from megano.catalog.models import Product
from django.utils.translation import gettext_lazy as _
from megano.coreapp.models.basemodel import BaseModel
from .order import Order


class OrderItem(BaseModel):

    """Модель товара в Заказе пользователя"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="order_item"
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
