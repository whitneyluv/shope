from django.views.generic import TemplateView


class CartView(TemplateView):
    """Отображение корзины пользователя"""
    template_name = "cart_app/cart.html"
    context_object_name = 'cart'
