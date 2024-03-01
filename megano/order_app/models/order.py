from django.db import models
from megano.coreapp.models.basemodel import BaseModel
from megano.auth_app.models.user import User


class Order(BaseModel):

    """ Модель заказа """

    DELIVERY_CHOICES = [
        ('f', 'free_delivery'),
        ('p', 'payed_delivery'),
        ('sd', 'self-delivery')
    ]

    PAYMENT_TYPE_CHOICES = [
        ("c", 'card'),
        ('ch', 'cash'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('p', "paid"),
        ('unp', "unpaid")
    ]

    fio = models.CharField(max_length=50, verbose_name='fio')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='order')
    delivery_type = models.CharField(max_length=3, choices=DELIVERY_CHOICES, default='sd', verbose_name="delivery_type")
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name='city')
    address = models.TextField(max_length=100, null=True, blank=True, verbose_name='city')
    payment_type = models.CharField(max_length=3, choices=PAYMENT_TYPE_CHOICES,
                                    default='c', verbose_name="payment_type")
    payment_status = models.CharField(max_length=3, choices=PAYMENT_STATUS_CHOICES,
                                      default="unp", verbose_name="payment_status")
    total_amount = models.DecimalField(max_digits=20, blank=True, null=False, decimal_places=2, verbose_name='total_amount')


class OrderItem(BaseModel):

    """Модель товара в корзине пользователя"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="order_items",
        verbose_name="order_item"
    )
