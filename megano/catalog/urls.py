from django.urls import path
from .views import catalog_page, comparison_page

app_name = 'catalog'

urlpatterns = [
    path('', catalog_page, name='catalog'),
    path('comparison/', comparison_page, name='comparison'),
]