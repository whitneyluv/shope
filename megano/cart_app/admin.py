from django.contrib import admin
from .models import Cart, CartItem


class CartItemInline(admin.TabularInline):
    """Отображение и редактирование экземпляров
    модели CartItem в интерфейсе модели Cart в админке"""
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """Регистрация модели Cart в админке"""
    readonly_fields = 'total_amount',
    inlines = [CartItemInline]
    ordering = ["user"]


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Регистрация модели CartItem в админке"""
    ordering = ["cart"]
