# from megano.wsgi import *
from discounts_app.services.cart_discount_calculations import CartDiscountCalculations
from discounts_app.interfaces.discounts_interface import IDiscounts
import inject


class ProductDiscountCalculations:
    _discount: IDiscounts = inject.attr(IDiscounts)

    @classmethod
    def apply_product_discount(cls, cart: list):
        """
        Функция последовательно применяет возможные скидки к каждому товару из корзины
        """

        product_discounts = cls._discount.get_all_active_product_discounts()
        if product_discounts:
            for item in cart:
                for discount in product_discounts:

                    if item['product_id'] == discount.product.id and item['seller_id'] == discount.seller.all()[0].id:
                        new_price = CartDiscountCalculations.apply_discount(discount, item['price'])
                        item['price'] = new_price

            result = CartDiscountCalculations.calculate_cart_sum(cart)

            return result
        else:
            return None
