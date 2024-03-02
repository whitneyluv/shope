from django.db import models
from coreapp.models.basemodel import BaseModel
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from profile_app.models.seller import Seller


class Category(models.Model):
    """
    Модель категории товара
    """

    def __str__(self):
        return f'Модель категории {self.title}'

    title = models.CharField(verbose_name=_('title'), max_length=30, unique=True, blank=False)
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to=f'categories/{title.verbose_name}/%Y/%m/%d',
        blank=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )


def product_images_directory_path(instance: 'Product', filename: str) -> str:
    return f'product/product{instance.category.pk}/images/{filename}'


class Product(BaseModel):

    title = models.CharField(max_length=30, null=True, blank=True, verbose_name='title')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(upload_to=product_images_directory_path, verbose_name='images')
    tag = TaggableManager()
    is_limited = models.BooleanField(default=False, verbose_name='is_limited')
    free_delivery = models.BooleanField(default=True, verbose_name='free_delivery')


class Price(BaseModel):
    price = models.FloatField(null=True, blank=True, verbose_name='price')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='prices')
