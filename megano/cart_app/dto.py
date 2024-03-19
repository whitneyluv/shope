import inject
from typing import List
from dataclasses import dataclass
from decimal import Decimal
from profile_app.interfaces import ISeller
from catalog.interfaces import IProduct


@dataclass
class Seller:
    id: int = 0
    name: str = ''
    _seller: ISeller = inject.attr(ISeller)

    def session_init(self, seller_id: int):
        seller = self._seller.get_seller(seller_id)
        self.id = seller.pk
        self.name = seller.name
        return self

    def authenticated_user_init(self, seller):
        self.id = seller.pk
        self.name = seller.name
        return self


@dataclass
class Product:
    id: int = 0
    title: str = ''
    description: str = ''
    image: str = ''
    _product: IProduct = inject.attr(IProduct)

    def session_init(self, product_id: int):
        product = self._product.get_product(product_id)
        self.id = product.pk
        self.title = product.title
        self.description = product.description
        self.image = product.product_images.first().image.url
        return self

    def authenticated_user_init(self, product):
        self.id = product.pk
        self.title = product.title
        self.description = product.description
        self.image = product.product_images.first().image.url
        return self


@dataclass
class CartItemDTO:
    seller: Seller
    product: Product
    quantity: int


@dataclass
class CartDTO:
    cart_items: List[CartItemDTO]
    total_amount: Decimal
