from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    Модель профиля пользователя
    """

    def __str__(self):
        return f'Модель профиля для пользователя {self.user}'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField()
