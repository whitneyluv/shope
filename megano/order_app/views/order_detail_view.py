from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView
from order_app.interface.order_interface import IOrder
import inject
from order_app.services.create_payment import OrderPayment
from order_app.models.order import Order


class OrderDetailView(DetailView):

    _order: IOrder = inject.attr(IOrder)
    template_name = "order_app/oneorder.html"
    context_object_name = "order"
    queryset = Order.objects.all()

    @method_decorator(csrf_exempt)
    def get_context_data(self, **kwargs):
        """Формирует контекст для шаблона"""
        order = self._order.get_order_by_pk(pk=self.kwargs['pk'])
        order_items = self._order.get_order_items(order_pk=order.pk)
        confirmation_url = ''
        if order.payment_status != "paid":
            payment = OrderPayment.payment_create(order_pk=order.pk)
            order.payment_id = payment.id
            order.save()
            confirmation_url = payment.confirmation.confirmation_url

        context = super().get_context_data(**kwargs)
        context['order'] = order
        context['order_items'] = order_items
        context['confirmation_url'] = confirmation_url
        return context
