from django.db import models
from django.conf import settings


class Profile(models.Model):
    """
    Модель профиля пользователя
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    avatar = models.ImageField()
