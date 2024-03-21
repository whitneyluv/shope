import inject
from typing import List
from dataclasses import dataclass
from decimal import Decimal
from profile_app.interfaces import ISeller
from catalog.interfaces import IProduct


@dataclass
class Seller(object):
    """
    модель DTO для модели Seller
    """
    pk: int = 0
    name: str = ''
    _seller: ISeller = inject.attr(ISeller)


@dataclass
class Product(object):
    """
    модель DTO для модели Product
    """
    pk: int = 0
    title: str = ''
    description: str = ''
    image: str = ''
    _product: IProduct = inject.attr(IProduct)


@dataclass
class CartItemDTO:
    """
    модель DTO для модели CartItem
    """
    seller: Seller
    product: Product
    quantity: int


@dataclass
class CartDTO:
    """
    модель DTO для модели Cart
    """
    cart_items: List[CartItemDTO]
    total_amount: Decimal
