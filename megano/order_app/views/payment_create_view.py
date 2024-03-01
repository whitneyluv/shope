from django.shortcuts import render, redirect
from django.views import View
from megano.order_app.services.create_payment import OrderPayment


class PaymentCreateView(View):

    def get(self, request, order_pk=1):

        conformation_url = OrderPayment.payment_create(order_pk=order_pk)

        return redirect(conformation_url)
