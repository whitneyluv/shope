from django.contrib import admin
from .models.banner import Banner


@admin.register(Banner)
class BannerInline(admin.ModelAdmin):
    """Добавление характеристики в админке модели Banner"""


