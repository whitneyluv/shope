from django.db import models
from django.utils.translation import gettext_lazy as _

CHOICES = [
    ('p', _('Per cent')),
    ('f', _('Fixed amount')),
    ('fp', _('Fixed price')),]


class BaseModel(models.Model):
    """Модель Базовая"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('creation time'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))
    is_active = models.BooleanField(default=True, verbose_name=_('active'))

    class Meta:
        abstract = True


class Banner (BaseModel):

    """Модель Баннера на главной странице """

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='banners')
    title = models.CharField(max_length=30, null=True, blank=True, verbose_name='banner_title')
    text = models.TextField(max_length=200, null=True, blank=True, verbose_name='banner_text')
    footer_text = models.CharField(max_length=30, null=True, blank=True, verbose_name='banner_footer')
    image = models.ImageField(upload_to='banners', null=True, blank=True, verbose_name='banner_image')
    link = models.TextField(null=False, blank=False, verbose_name='banner_link')


class Product(BaseModel):
    pass
    # seller = models.ManyToManyField(Seller, on_delete=models.CASCADE, related_name='products' )
    # set = models.ForeignKey(ProductSet,on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(verbose_name="price", default=0)


class ProductSet(BaseModel):

    """Модель товарного набора"""

    # group_1 = models.ManyToManyField(Product, on_delete=models.CASCADE, related_name='product_sets')
    # group_2 = models.ManyToManyField(Product, on_delete=models.CASCADE, related_name='product_sets')
    # discount = models.ForeignKey(SetDiscount, on_delete=models.CASCADE, related_name='set_discount')
    # class Meta:
    #          verbose_name = 'Set'
    #          verbose_name_plural = 'Sets'


class BaseDiscount(models.Model):

    """Базовая модель скидки """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('creation time'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))
    is_active = models.BooleanField(default=True, verbose_name=_('active'))
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='name')
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name='description')
    type_of_discount = models.CharField(max_length=2, choices=CHOICES, default='p', verbose_name='type')
    amount = models.FloatField(verbose_name="amount", default=0)

    class Meta:
        abstract = True


class ProductDiscount(BaseDiscount):

    """Модель скидки на товар """

    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_discounts')
    # seller = models.ManyToManyField(Seller, on_delete=models.CASCADE, related_name='product_discounts')

    class Meta:
        verbose_name = _('product discount')
        verbose_name_plural = _('product discounts')


class SetDiscount(BaseDiscount):
    # set = models.ForeignKey(ProductSet, on_delete=models.CASCADE, related_name='set_discount')

    class Meta:
        verbose_name = _('set discount')
        verbose_name_plural = _('set discounts')


class CartDiscount(BaseDiscount):
    pass

    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_discount')
