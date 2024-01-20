from django.views.generic.base import TemplateView


class CartView(TemplateView):
    """Отображение корзины пользователя"""
    template_name = "cart_app/cart.html"
