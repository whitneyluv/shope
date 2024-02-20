from django.db import models
from coreapp.models.basemodel import BaseModel
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _
from profile_app.models.seller import Seller


def product_images_directory_path(instance: 'Product', filename: str) -> str:
    """Формирует путь к файлу с изображением продукта"""
    return (f'products/category-{instance.product.category.pk}/'
            f'images/product-{instance.product.pk}_{filename}')


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
    """Продукт"""
    title = models.CharField(max_length=30, null=True, blank=True, verbose_name='title')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    description = models.TextField(
        max_length=256,
        null=True,
        blank=True,
        verbose_name=_('description')
    )
    characteristic = models.ManyToManyField(
        'Characteristic',
        through='ProductCharacteristic',
        related_name='products',
        verbose_name=_('characteristic')
    )
    tag = TaggableManager()
    is_limited = models.BooleanField(default=False, verbose_name='is_limited')
    free_delivery = models.BooleanField(default=True, verbose_name='free_delivery')

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title


class ProductImage(BaseModel):
    """Изображение продукта"""
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_images',
        verbose_name=_('product')
    )
    image = models.ImageField(upload_to=product_images_directory_path, verbose_name=_('image'))
    description = models.TextField(blank=True, max_length=2048, verbose_name=_('description'))

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')


class Price(BaseModel):
    """Цена продукта"""
    price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=False,
        blank=True,
        default=0,
        verbose_name=_('price')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='prices')

    def __str__(self):
        return f'{self.product} | {self.price}'


class Characteristic(BaseModel):
    """Характеристика продукта"""
    title = models.CharField(max_length=64, verbose_name=_('title'))

    class Meta:
        verbose_name = _('characteristic')
        verbose_name_plural = _('characteristics')

    def __str__(self):
        return self.title


class ProductCharacteristic(models.Model):
    """Значение характеристики продукта"""
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name='product_characteristics',
        verbose_name=_('product')
    )
    characteristic = models.ForeignKey(
        Characteristic,
        on_delete=models.PROTECT,
        related_name='product_characteristics',
        verbose_name=_('characteristic')
    )
    value = models.CharField(max_length=128, verbose_name=_('value'))

    class Meta:
        verbose_name = _('product characteristic')
        verbose_name_plural = _('product characteristics')

    def __str__(self):
        return f'{self.product} | {self.characteristic}'
