from django import forms
from .models.order import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "fio", "user", "delivery_type", "city", "address", "payment_type", "payment_status", "total_amount"