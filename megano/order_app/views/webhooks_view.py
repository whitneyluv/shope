import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from yookassa import Configuration, Payment
from yookassa.domain.notification import WebhookNotificationEventType, WebhookNotificationFactory
# from yookassa.domain.common import SecurityHelper
from order_app.services.confimation_payment import PaymentConfirmation
@csrf_exempt
def my_webhook_handler(request):
    # # Если хотите убедиться, что запрос пришел от ЮКасса, добавьте проверку:
    # ip = get_client_ip(request)  # Получите IP запроса
    # if not SecurityHelper().is_ip_trusted(ip):
    #     return HttpResponse(status=400)

    # Извлечение JSON объекта из тела запроса
    event_json = json.loads(request.body)
    try:
        # Создание объекта класса уведомлений в зависимости от события
        notification_object = WebhookNotificationFactory().create(event_json)
        response_object = notification_object.object
        print(response_object)
        if notification_object.event == WebhookNotificationEventType.PAYMENT_SUCCEEDED:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.PAYMENT_WAITING_FOR_CAPTURE:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.PAYMENT_CANCELED:
            some_data = {
                'paymentId': response_object.id,
                'paymentStatus': response_object.status,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.REFUND_SUCCEEDED:
            some_data = {
                'refundId': response_object.id,
                'refundStatus': response_object.status,
                'paymentId': response_object.payment_id,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.DEAL_CLOSED:
            some_data = {
                'dealId': response_object.id,
                'dealStatus': response_object.status,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.PAYOUT_SUCCEEDED:
            some_data = {
                'payoutId': response_object.id,
                'payoutStatus': response_object.status,
                'dealId': response_object.deal.id,
            }
            # Специфичная логика
            # ...
        elif notification_object.event == WebhookNotificationEventType.PAYOUT_CANCELED:
            some_data = {
                'payoutId': response_object.id,
                'payoutStatus': response_object.status,
                'dealId': response_object.deal.id,
            }
            # Специфичная логика
            # ...
        else:
            # Обработка ошибок
            print("Error on indentifing")
            return HttpResponse(status=400)  # Сообщаем кассе об ошибке

        # Специфичная логика
        # ...
        print(some_data)
        Configuration.configure('325975', 'test_ickkaiUFF3G5QKquognLgIOjSKCLEevmyGJc8Vk_u_Y')
        # Получим актуальную информацию о платеже
        payment_info = Payment.find_one(some_data['paymentId'])
        print(list(payment_info))
        if payment_info:
            if PaymentConfirmation.confirm_payment(payment_info):
                print('ну надо жЕ! РАБОТАЕТ!')
                return HttpResponse(status=200)
            else:
                print('оплата не прошла')
                return HttpResponse(status=400)  # Сообщаем кассе об ошибке

    except Exception as e:
        print(e,'ошибка наверно здесь')
        return HttpResponse(status=400)  # Сообщаем кассе об ошибке
