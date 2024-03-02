from django.contrib import admin
from .models import (
    Product,
    Category,
    Price,
    Characteristic,
    ProductCharacteristic,
    ProductImage,
    Review,
    RecentlyViewedProducts
)


class ProductCharacteristicInline(admin.StackedInline):
    """Добавление характеристики в админке модели Product"""
    model = ProductCharacteristic


class ProductImageInline(admin.StackedInline):
    """Добавление изображения в админке модели Product"""
    model = ProductImage


class ProductReviewInline(admin.StackedInline):
    """Добавление отзыва в админке модели Product"""
    model = Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Регистрация модели Category в админке"""
    ordering = 'title',


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    """Регистрация модели Price в админке"""
    ordering = 'product',


@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    """Регистрация модели Characteristic в админке"""
    ordering = 'title',


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """Регистрация модели Review в админке"""
    ordering = 'author',


@admin.register(RecentlyViewedProducts)
class RecentlyViewedProductsAdmin(admin.ModelAdmin):
    """Регистрация модели RecentlyViewedProducts в админке"""
    ordering = 'user', '-updated_at'


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#
#     actions = ['clear_cache']
#
#         def clear_cache(self, request, queryset):
#             for product in queryset:
#                 cache_key = f'catalog_{product.category_id}_products'
#                 cache.delete(cache_key)
#             self.message_user(request, f'Cache cleared for {queryset.count()} products.')
#
#     clear_cache.short_description = "Clear cache for selected products"
