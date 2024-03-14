from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from cart_app.models import Cart, CartItem
from order_app.models.order import Order
from order_app.models.order_item import OrderItem
from discounts_app.services.discount_processing import DiscountProcessing


class CreateOrderView(View, LoginRequiredMixin):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'order_app/order.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        user = request.user
        cart_items = CartItem.objects.filter(cart__user=user.pk)

        order = Order.objects.create(
            user=user,
            fio=request.POST.get('name'),
            delivery_type=request.POST.get('delivery'),
            city=request.POST.get('city'),
            address=request.POST.get('address'),
            payment_type=request.POST.get('pay'),
            total_amount=DiscountProcessing.get_cart_sum_with_discounts(user_id=user.pk)
        )
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                seller=cart_item.seller)
        order.save()

        return redirect('order_details', pk=order.pk)

