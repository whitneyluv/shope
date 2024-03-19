from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from cart_app.models import Cart, CartItem
from order_app.models.order import Order
from order_app.models.order_item import OrderItem
from discounts_app.services.discount_processing import DiscountProcessing
from order_app.interface.order_interface import IOrder
import inject
from order_app.forms import OrderForm


class CreateOrderView(View, LoginRequiredMixin):

    _order: IOrder = inject.attr(IOrder)

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'order_app/order.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        user = request.user
        cart_items = self._order.get_cart_items(user_pk=user.pk)
        data = {
            'user': user,
            'fio': request.POST.get('name'),
            'delivery_type': request.POST.get('delivery'),
            'city': request.POST.get('city'),
            'address': request.POST.get('address'),
            'payment_type': request.POST.get('pay'),
            'total_amount': DiscountProcessing.get_cart_sum_with_discounts(user_id=user.pk)
        }
        form = OrderForm(data)

        if form.is_valid():
            order = form.save()

            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    seller=cart_item.seller)
                self._order.delete_cart_item_from_cart(cart_item)

            self._order.save(order)
        else:
            return render(request, 'order_app/order.html')
        return redirect('order_details', pk=order.pk)

