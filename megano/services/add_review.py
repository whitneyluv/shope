from typing import Dict, List


class ReviewService:
    def add_review_to_product(self, user_id, product_id, rating, comment):
        # Метод-заглушка для добавления отзыва к товару
        pass

    def get_reviews_for_product(self, product_id) -> List[Dict]:
        # Метод-заглушка для получения списка отзывов к товару
        pass

    def get_discount_for_cart(self, cart_items: List[Dict]) -> Dict:
        # Метод-заглушка для получения скидки на корзину
        pass

    def get_review_count_for_product(self, product_id) -> int:
        # Метод-заглушка для получения количества отзывов к товару
        pass
