from django.urls import path
from .views.catalog_filters import CatalogPageView, ComparisonPageView


app_name = 'catalog'

urlpatterns = [
    path('', CatalogPageView.as_view(template_name='catalog/catalog.html'), name='catalog'),
    path('comparison/', ComparisonPageView.as_view(template_name='catalog/comparison.html'), name='comparison'),
]
