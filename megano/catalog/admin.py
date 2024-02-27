from django.contrib import admin
from .models import Product, Category, Price


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
    # actions = ['clear_cache']
    #
    # # def clear_cache(self, request, queryset):
    # #     for product in queryset:
    # #         cache_key = f'catalog_{product.category_id}_products'
    # #         # cache.delete(cache_key)
    # #     self.message_user(request, f'Cache cleared for {queryset.count()} products.')
    #
    # clear_cache.short_description = "Clear cache for selected products"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    pass
