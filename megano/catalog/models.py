from django.db import models
from coreapp.models import BaseModel
from taggit.managers import TaggableManager


class Seller(BaseModel):
    pass


class Category(BaseModel):
    pass


def product_images_directory_path(instance: 'Product', filename: str) -> str:
    return 'product/product{pk}/images/{filename}'.format(
        pk=instance.product.pk,
        filename=filename)


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
