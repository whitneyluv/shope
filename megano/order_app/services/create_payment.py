"""
Сценарий проведения платежа
Пользователь переходит к оплате.
Вы отправляете ЮKassa запрос на создание платежа.
ЮKassa возвращает вам созданный объект платежа с токеном для инициализации виджета.
Вы инициализируете виджет и отображаете форму на странице оплаты или во всплывающем окне.
Пользователь выбирает способ оплаты, вводит данные.
При необходимости виджет перенаправляет пользователя на страницу подтверждения платежа или отображает всплывающее окно (например, для аутентификации по 3‑D Secure).
Пользователь подтверждает платеж.
Если по какой-то причине платеж не прошел (например, не хватило денег) и срок действия токена для инициализации виджета еще не истек, виджет отображает пользователю сообщение об ошибке и предлагает оплатить еще раз с возможностью повторно выбрать способ оплаты.
Если пользователь подтвердил платеж или если закончился срок действия токена для инициализации, виджет перенаправляет пользователя на страницу завершения оплаты на вашей стороне или выполняет действия, настроенные вами для события завершения оплаты.
Вы отображаете нужную информацию, в зависимости от статуса платежа.
Готово!

"""

import var_dump as var_dump
from yookassa import Payment, Configuration
import inject
from megano.order_app.interface.order_interface import IOrder


Configuration.configure('325975', 'test_ickkaiUFF3G5QKquognLgIOjSKCLEevmyGJc8Vk_u_Y')
RETURN_URL = 'https://google.com/'


class OrderPayment:

    _order: IOrder = inject.attr(IOrder)

    @classmethod
    def payment_create(cls, order_pk):

        order = cls._order.get_order_by_pk(order_pk)

        res = Payment.create(
            {
                "amount": {
                    "value": order.total_amount,
                    "currency": "RUB"
                },
                "confirmation": {
                    "type": "redirect",
                    "return_url": RETURN_URL,
                },
                "capture": True,
                "description": f"Заказ №{order.pk}",
                "metadata": {
                    'orderNumber': order.pk,
                    'user_id': order.user.id,
                },
            })

        order.payment_id = res.id
        order.save()
        var_dump.var_dump(res)

        return res.confirmation.confirmation_url


# def payment_info(payment_id):
#     res = Payment.find_one(payment_id)
#
#     a = var_dump.var_dump(res)
#     return a


# order_item = Order.objects.get(pk=1)
# print(order_item)
# a = payment_create(order_item)
# print(a)

# b = payment_info('2d4b380d-000f-5000-8000-1c40aa5a7407')
# print(b)
