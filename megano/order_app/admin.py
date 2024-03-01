from django.contrib import admin
from megano.order_app.models.order import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

