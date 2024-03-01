from django.core.exceptions import ObjectDoesNotExist
from yookassa import Payment
from payment_app.models.paymentdata import PaymentData
from order_app.models.order import Order
import var_dump as var_dump


class PaymentConfirmation:

    @classmethod
    def payment_info(cls, payment_id):
        res = Payment.find_one(payment_id)
        return res

    @classmethod
    def confirm_payment(cls, order_pk):

        try:
            order = Order.objects.get(id=order_pk)
            payment_id = order.payment_id
            order_payment = cls.payment_info(payment_id)
        except ObjectDoesNotExist:
            raise "Такого заказа нет"

        if order_payment.status == 'succeeded':
            order.payment_status = 'p'
            order.save()
            return True
        else:
            return False

    # def confirm_payment(order_id):
    #
    #     try:
    #         current_payment = PaymentData.objects.get(id=response['metadata']['orderNumber'])
    #
    #     except ObjectDoesNotExist:
    #         raise "Такого заказа нет"
    #
    #     if response['event'] == 'payment.succeeded':
    #         current_payment.payment_status = 'p'
    #         current_payment.order.payment_status = 'p'
    #         current_payment.save()
    #         return True
    #     elif response['event'] == 'payment.canceled':
    #         return False
