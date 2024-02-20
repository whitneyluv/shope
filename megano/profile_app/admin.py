from django.contrib import admin

from .models.seller import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    ordering = 'name',
