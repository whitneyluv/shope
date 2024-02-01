from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models
from .usermanager import NewUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Новая модель пользователя
    """

    def __str__(self):
        return f'Модель для пользователя {self.email}'

    username = models.CharField(_('username'), max_length=150, unique=False, blank=True)
    email = models.EmailField(
        max_length=60,
        unique=True,
        error_messages={
            "unique": _("Пользователь с таким email уже существует"),
        }
    )
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True)
    activation_key = models.CharField(max_length=60, blank=True)
    activation_name_set = models.CharField(max_length=60, blank=True)
    is_activation_key_expires = models.BooleanField(default=False)

    objects = NewUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
