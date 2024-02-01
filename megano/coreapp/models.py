from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):

    """Модель Базовая"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('creation time'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated time'))
    is_active = models.BooleanField(default=True, verbose_name=_('active'))

    class Meta:
        abstract = True


class Setting(BaseModel):
    """Модель для хранения настроек"""
    key = models.CharField(max_length=255, unique=True, verbose_name='key')
    value = models.TextField(verbose_name='value')

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.key


def banner_images_directory_path(instance: 'Banner', filename: str) -> str:
    return 'banners/banner_{pk}/{filename}'.format(pk=instance.pk, filename=filename)


class Banner (BaseModel):

    """Модель Баннера на главной странице """

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    title1 = models.CharField(max_length=30, null=True, blank=True, verbose_name='banner_title1')
    title2 = models.CharField(max_length=30, null=True, blank=True, verbose_name='banner_title2')
    title3 = models.CharField(max_length=30, null=True, blank=True, verbose_name='banner_title3')
    text = models.TextField(max_length=200, null=True, blank=True, verbose_name='banner_text')
    button = models.CharField(max_length=30, null=True, blank=True, default="Get Started", verbose_name='banner_footer')
    image = models.ImageField(upload_to=banner_images_directory_path, null=True, blank=True, verbose_name='banner_image')
    link = models.URLField(null=True, blank=True, verbose_name='banner_link')
