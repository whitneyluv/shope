# from megano.wsgi import *
from discounts_app.models import ProductDiscount
from cart_discount_calculations import apply_discount, calculate_cart_sum


def apply_product_discount(cart: list):
    """
    Функция последовательно применяет возможные скидки к каждому товару из корзины
    """

    product_discounts = ProductDiscount.objects.all().filter(is_active=True)
    if product_discounts:
        for item in cart:
            for discount in product_discounts:

                if item['product_id'] == discount.product.id and item['seller_id'] == discount.seller.all()[0].id:
                    new_price = apply_discount(discount, item['price'])
                    item['price'] = new_price

        result = calculate_cart_sum(cart)

        return result
    else:
        return None
