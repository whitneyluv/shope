from django.shortcuts import render
from django.views import View
from order_app.services.confimation_payment import PaymentConfirmation


class PaymentResult(View):

    def get(self, request):

        result = PaymentConfirmation.confirm_payment(order_pk=self.kwargs['pk'])
        if result:
            context = {'message': "Оплата успешно прошла!"}
        else:
            context = {'message': "Оплата не прошла Попробуйте еще раз"}

        return render(request, 'order_app/payment_result.html', context=context)
