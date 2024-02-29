import inject

from auth_app.models.user import User
from cart_app.interfaces.cart_interface import ICart
from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.models import CartItem
from cart_app.repositories.cart_item_repositories import CartItemRepository
from cart_app.repositories.cart_repositories import CartRepository
from catalog.interfaces.product_interface import IProduct
from catalog.repositories.product_repositories import ProductRepository
from profile_app.interfaces.seller_interface import ISeller
from profile_app.repositories.seller_repositories import SellerRepository


class AddProductsToCart:
    """Класс для реализации методов добавления товаров в корзину"""
    __product: IProduct = inject.attr(ProductRepository)
    __seller: ISeller = inject.attr(SellerRepository)
    __cart: ICart = inject.attr(CartRepository)
    __cart_item: ICartItem = inject.attr(CartItemRepository)

    def __init__(self, user: User) -> None:
        self.cart = self.__cart.get_cart_by_user(user=user)

    def __call__(self, quantity: int, product_id: int, seller_id: int) -> None:
        """Метод добавления товаров в корзину"""
        self.__cart_item.save(
            CartItem(
                cart=self.cart,
                product=self.__product.get_product(pk=product_id),
                seller=self.__seller.get_seller(pk=seller_id),
                quantity=quantity
            )
        )
