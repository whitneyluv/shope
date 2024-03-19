from beartype import beartype
from order_app.models.order_item import OrderItem
from order_app.interface.order_item_interface import IOrderItem


class OrderItemRepository(IOrderItem):

    @beartype
    def get_order_items(self, order_pk):
        return OrderItem.objects.filter(order_id=order_pk)
