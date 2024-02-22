# from megano.wsgi import *
from discounts_app.models.cart_discount import CartDiscount
from cart_app.models import CartItem
from catalog.models import Price


def apply_discount(discount, price):

    """Расчет скидки на товар/корзину в зависимости от типа скидки"""

    if discount.type_of_discount == 'per':
        percent_of_discount = discount.amount / 100
        final_price = price * (1 - percent_of_discount)
        return final_price

    elif discount.type_of_discount == 'fa':
        fixed_discount = discount.amount
        if price <= fixed_discount:
            final_price = 1

        else:
            final_price = price - fixed_discount
        return final_price

    else:
        fixed_price_for_product = discount.amount

        return fixed_price_for_product


def calculate_cart_sum(cart: list):

    """ Подсчет итоговой цены корзины"""

    total_sum = 0
    for product in cart:
        total_sum += product['price'] * product['quantity']

    return total_sum


def check_conditions_cart_discount(discount, cart: list):

    """Проверка соблюдения условий скидки на корзину"""

    cart_sum = calculate_cart_sum(cart)
    if len(cart) >= discount.products_quantity:
        return True
    elif discount.final_sum_max >= cart_sum >= discount.final_sum_min:
        return True
    else:
        return False


def apply_cart_discount(cart: list):

    """Расчет минимальной цены корзины со скидкой"""

    total_sum_of_cart = []
    all_active_cart_discounts = CartDiscount.objects.filter(is_active=True).all()
    res = calculate_cart_sum(cart)

    if all_active_cart_discounts:
        for discount in all_active_cart_discounts:
            if check_conditions_cart_discount(discount, cart):
                result = apply_discount(discount, res)
            else:
                result = res
            total_sum_of_cart.append(result)

        return min(total_sum_of_cart)
    else:
        return None


def get_items_with_prices(user_id) -> list:

    """
    Обрабатывает корзину, формирует список товаров в корзине с ценой и количеством

    """

    cart_items = CartItem.objects.values().filter(cart__user=user_id)

    ids = []
    cart_data = []

    for item in cart_items:
        ids.append(item['product_id'])

        data_to_add = {
            'item_id': item['id'],
            'product_id': item['product_id'],
            'quantity': item['quantity'],
            'seller_id': item['seller_id']
        }
        cart_data.append(data_to_add)

    prices_for_cart = Price.objects.values().filter(product__id__in=ids)
    for cart_item in cart_data:
        for price in prices_for_cart:
            if cart_item['product_id'] == price['product_id'] and cart_item['seller_id'] == price['seller_id']:
                cart_item['price_id'] = price['id']
                cart_item['price'] = price['price']
    return cart_data


a = Price.objects.all().prefatch_related('product').filter(product_id=1)
print(a)
