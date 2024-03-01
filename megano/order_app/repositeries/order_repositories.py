from beartype import beartype
from megano.order_app.interface.order_interface import IOrder
from megano.order_app.models.order import Order
from django.shortcuts import get_object_or_404


class OrderRepository(IOrder):

    @beartype
    def save(self, model: Order):
        model.save()

    @beartype
    def get_order_by_pk(self, pk):
        return Order.objects.get(pk=pk)
