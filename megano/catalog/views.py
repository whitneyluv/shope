from django.views import generic
from .models import Product


class ProductDetailViews(generic.DetailView):
    """Представление для отображения детальной страницы товара"""
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"
