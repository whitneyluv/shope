from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Seller(models.Model):
    """
    Модель профиля продавца
    """

    def __str__(self):
        return f'Модель профиля для продавца {self.user}'

    def get_email(self):
        return self.user.email

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=256, unique=True)
    logo = models.ImageField(
        _('Logotype'),
        upload_to=f'seller/{get_email}/%Y/%m/%d',
        blank=True
    )
    description = models.TextField(_('Description'), blank=True)
