from typing import List
from dataclasses import dataclass


@dataclass
class Seller:
    id: int
    name: str


@dataclass
class Product:
    id: int
    title: str
    description: str
    image: str


@dataclass
class CartItemDTO:
    seller: Seller
    product: Product
    quantity: int


@dataclass
class CartDTO:
    cart_items: List[CartItemDTO]
    total_amount: int


# a = CartItemDTO(seller=Seller(id=1, name="seller1"),
#                 product=Product(id=2, name='product1', descrip='3123123', img='some_url')
#                 )
