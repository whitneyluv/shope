from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    actions = ['clear_cache']

    def clear_cache(self, request, queryset):
        for product in queryset:
            cache_key = f'catalog_{product.category_id}_products'
            cache.delete(cache_key)
        self.message_user(request, f'Cache cleared for {queryset.count()} products.')

    clear_cache.short_description = "Clear cache for selected products"
