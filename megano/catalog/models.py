from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """
    Модель категории товара
    """

    def __str__(self):
        return f'Модель категории {self.title}'

    title = models.CharField(verbose_name=_('title'), max_length=30, unique=True, blank=False)
    image = models.ImageField(
        verbose_name=_('image'),
        upload_to=f'categories/{title.verbose_name}/%Y/%m/%d',
        blank=True,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
