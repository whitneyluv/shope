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
    key = models.CharField(max_length=255, unique=True, verbose_name=_('key'))
    value = models.TextField(verbose_name=_('value'))
    cache = models.IntegerField(default=3000, verbose_name=_('cache'))
    debug = models.BooleanField(default=True, verbose_name=_('debug'))

    class Meta:
        verbose_name = _('Настройка')
        verbose_name_plural = _('Настройки')

    def __str__(self):
        return self.key

    def set_cache(self, new_cache_value):
        self.cache = new_cache_value
        self.save()
