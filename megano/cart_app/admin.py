from django.contrib import admin
from .models import Cart, ProductCart


class ProductCartInline(admin.TabularInline):
    """Отображение и редактирование экземпляров
    модели ProductCart в интерфейсе модели Cart в админке"""
    model = ProductCart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Регистрация модели Cart в админке"""
    inlines = [ProductCartInline]
    ordering = ["user"]


@admin.register(ProductCart)
class ProductCartAdmin(admin.ModelAdmin):
    """Регистрация модели ProductCart в админке"""
    ordering = ["cart"]
