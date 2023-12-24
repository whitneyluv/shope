from django.urls import path
from . import views

urlpatterns = [
    path('history/', views.history_order, name='history_order'),
    path('one/', views.one_order, name='one_order'),
    path('', views.order, name='order'),
]
