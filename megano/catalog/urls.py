from django.urls import path
from .views import ProductDetailViews


app_name = "catalog"

urlpatterns = [
    path("item/<int:pk>/", ProductDetailViews.as_view(), name='product_detail'),
]
