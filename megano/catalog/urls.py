from django.urls import path
from .views.catalog_filters import CatalogPageView, ComparisonPageView
from .views import  ProductDetailView


app_name = 'catalog'

urlpatterns = [
    path('', CatalogPageView.as_view(template_name='catalog/catalog.html'), name='catalog'),
    path('comparison/', ComparisonPageView.as_view(), name='comparison'),
    path('item/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
