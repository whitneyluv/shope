from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.db import models
from .usermanager import NewUserManager
from django.contrib.auth.models import PermissionsMixin


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
            "unique": _("A user with that username already exists."),
        }
    )
    middle_name = models.CharField(_('middle name'), max_length=30, blank=True)
    activation_key = models.CharField(max_length=60, blank=True)
    activation_name_set = models.CharField(max_length=60, blank=True)
    is_activation_key_expires = models.BooleanField(default=False)
    is_staff = models.BooleanField(
        default=False,
        verbose_name='staff status'
    )
    objects = NewUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
