from cart_app.models import Cart, CartItem
from catalog.models import Product
from profile_app.models.seller import Seller


class AddProductsToCart:
    """Класс для реализации методов добавления товаров в корзину"""

    def __init__(self, user_id: int) -> None:
        self.cart = Cart.objects.get(user=user_id)

    def __call__(self, quantity: int, product_id: int, seller_id: int) -> None:
        """Метод добавления товаров в корзину"""
        CartItem(
            cart=self.cart,
            product=Product.objects.get(id=product_id),
            seller=Seller.objects.get(id=seller_id),
            quantity=quantity
        ).save()
