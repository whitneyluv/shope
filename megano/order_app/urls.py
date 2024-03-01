from django.urls import path
from . import views
from .views.payment_create_view import PaymentCreateView
from .views.payment_result_view import PaymentResult

urlpatterns = [
    path('history/', views.history_order, name='history_order'),
    path('one/', views.one_order, name='one_order'),
    path('', views.order, name='order'),
    path("", PaymentCreateView.as_view()),
    path("payment_result/", PaymentResult.as_view()),
]
