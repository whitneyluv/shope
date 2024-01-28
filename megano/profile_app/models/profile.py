from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    Модель профиля пользователя
    """

    def __str__(self):
        return f'Модель профиля для пользователя {self.user}'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(_('phone number'), max_length=10, blank=True)
    avatar = models.ImageField(
        _('profile avatar'),
        upload_to=f'profiles/{user.email}/%Y/%m/%d',
        blank=True
    )
