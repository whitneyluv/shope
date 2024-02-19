from django.urls import path
from .views import CatalogPageView, ComparisonPageView


app_name = 'catalog'

urlpatterns = [
    path('', CatalogPageView.as_view(), name='catalog'),
    path('comparison/', ComparisonPageView.as_view(), name='comparison'),
]
