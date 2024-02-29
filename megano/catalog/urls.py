from django.urls import path
from .views import ProductDetailViews
from .views import catalog_page, comparison_page

app_name = "catalog"

urlpatterns = [
    path('', catalog_page, name='catalog'),
    path("item/<int:pk>/", ProductDetailViews.as_view(), name='product_detail'),
    path('comparison/', comparison_page, name='comparison'),
]