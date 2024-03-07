from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from order_app.forms import OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from cart_app.models import Cart, CartItem
from order_app.models.order import Order
from order_app.models.order_item import OrderItem
from discounts_app.services.discount_processing import DiscountProcessing
from order_app.services.create_payment import OrderPayment


class CreateOrderView(View):

    def create_order(self, request: HttpRequest) -> HttpResponse:

        if request.method == "POST":

            form = OrderForm(request.POST)
            if form.is_valid():
                user = request.user
                cart = user.cart
                cart_items = CartItem.objects.filter(cart=cart)
                try:
                    current_order = Order.objects.create(
                        user=user,
                        fio=form.fio,
                        delivery_type=form.delivery_type,
                        city=form.city,
                        address=form.address,
                        payment_type=form.payment_type,
                        total_amount=DiscountProcessing.get_cart_sum_with_discounts(user_id=user.pk)
                    )
                    for cart_item in cart_items:
                        OrderItem.objects.create(
                            order=current_order,
                            product=cart_item.product,
                            quantity=cart_item.quantity,
                            seller=cart_item.seller)
                    current_order.save()
                    conformation_url = OrderPayment.payment_create(order_pk=current_order.pk)
                    return redirect(conformation_url)
                except Exception as e:
                    print(str(e))
                    return JsonResponse({"Ошибка": "Произошла ошибка. Попробуйте еще раз"}, status=500)
        else:
            form = OrderForm()
            return render(request, 'order_app/order.html', {'form': form})