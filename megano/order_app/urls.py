from django.urls import path
from .views.payment_create_view import PaymentCreateView
from .views.payment_result_view import PaymentResult
from .views.order_create_view import CreateOrderView

urlpatterns = [
    # path('history/', views.history_order, name='history_order'),
    # path('one/', views.one_order, name='one_order'),
    path('', CreateOrderView.as_view()),
    path("payment", PaymentCreateView.as_view()),
    path("payment_result/", PaymentResult.as_view()),
]
