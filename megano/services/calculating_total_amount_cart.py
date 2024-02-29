from decimal import Decimal

import inject

from cart_app.interfaces.cart_item_interface import ICartItem
from cart_app.models import Cart
from cart_app.repositories.cart_item_repositories import CartItemRepository
from catalog.interfaces.price_interface import IPrice
from catalog.repositories.price_repositories import PriceRepository


class CalculatingTotalAmountCart:
    """Класс для реализации методов расчёта общей стоимости корзины"""

    __cart_item: ICartItem = inject.attr(CartItemRepository)
    __price: IPrice = inject.attr(PriceRepository)

    def __init__(self, cart: Cart) -> None:
        self.cart = cart

    def __call__(self) -> Decimal:
        """Метод расчёта общей стоимости корзины"""
        total_amount = Decimal("0.00")
        products = []
        sellers = []

        items = self.__cart_item.get_items_for_calc_total_amount_cart(cart=self.cart)
        [(products.append(item.product), sellers.append(item.seller)) for item in items]

        prices = self.__price.get_prices_for_calc_total_amount_cart(
            products=products, sellers=sellers)
        prices_dict = {(price.product.pk, price.seller.pk): price for price in prices}

        for item in items:
            price = prices_dict.get((item.product.pk, item.seller.pk))
            total_amount += item.quantity * price.price if price else 0
        return total_amount
