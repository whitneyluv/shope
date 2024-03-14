from django.urls import path
from .views.payment_create_view import PaymentCreateView
from .views.payment_result_view import PaymentResult
from .views.order_create_view import CreateOrderView
from .views.order_detail_view import OrderDetailView
from .views.webhooks_view import my_webhook_handler
from .views.history_order_view import HistoryOrdersView

urlpatterns = [
    path('', CreateOrderView.as_view()),
    path('<int:pk>/', OrderDetailView.as_view(), name='order_details'),
    path('history/', HistoryOrdersView.as_view(), name='history'),
    path("<int:pk>/payment/", PaymentResult.as_view()),
    path("payment-notification/",my_webhook_handler, name='webhook')
]
