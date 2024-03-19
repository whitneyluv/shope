import inject
from cart_app.interfaces.cart_item_interface import ICartItem
from services.dto_calculating_total_amount_cart import DTOCalculatingTotalAmountCart
from cart_app.dto import Product, Seller, CartDTO, CartItemDTO
from cart_app.models import CartItem


def quantity_products_and_total_amount_in_cart(request):
    """
    Функция получения информации об общей стоимости корзины, количестве товаров в ней и о самих товарах
    "amount_products_in_cart": Количество товаров в корзине,
    "total_amount_cart": Общая стоимость корзины,
    "cart": Экземпляр DTO модели 'Cart' которая содержит в себе все продукты
    """
    # _cart_items: ICartItem = inject.attr(ICartItem)
    cart_items = list()
    amount_products_in_cart = 0

    if request.user.is_authenticated:
        """
        Получение продуктов из базы данных если пользователь авторизирован
        """
        # for item in _cart_items.get_all_items_in_cart(request.user.cart):
        for item in CartItem.objects.filter(cart=request.user.cart):
            product = Product().db_user_init(item.product)
            seller = Seller().db_user_init(item.seller)
            amount_products_in_cart += item.quantity
            cart_items.append(CartItemDTO(seller=seller, product=product, quantity=item.quantity))
    else:
        """
            Получение продуктов из сессий если пользователь неавторизирован
        """
        if request.session.get('cart'):
            for item in request.session.get('cart'):
                amount_products_in_cart += item['num_products']
                product = Product().session_init(item['product_id'])
                seller = Seller().session_init(item['seller_id'])
                cart_items.append(CartItemDTO(seller=seller, product=product, quantity=item['num_products']))
    cart = CartDTO(cart_items=cart_items, total_amount=DTOCalculatingTotalAmountCart(cart_items)())
    return {
        "amount_products_in_cart": amount_products_in_cart,
        "total_amount_cart": cart.total_amount,
        "cart": cart
    }
