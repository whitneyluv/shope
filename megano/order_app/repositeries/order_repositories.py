from beartype import beartype
from order_app.interface.order_interface import IOrder
from order_app.models.order import Order
from order_app.models.order_item import OrderItem
from cart_app.models import CartItem


class OrderRepository(IOrder):

    @beartype
    def save(self, model: Order):
        model.save()

    @beartype
    def get_order_by_pk(self, pk):
        return Order.objects.get(pk=pk)

    @beartype
    def get_order_items(self, order_pk):
        return OrderItem.objects.filter(order_id=order_pk)

    @beartype
    def get_all_users_orders(self, user_pk):
        return Order.objects.filter(user_id=user_pk)

    @beartype
    def get_all_orders(self):
        return Order.objects.all()

    @beartype
    def get_cart_items(self, user_pk):
        return CartItem.objects.filter(cart__user=user_pk)

    @beartype
    def delete_cart_item_from_cart(self, cart_item):
        cart_item.delete()

