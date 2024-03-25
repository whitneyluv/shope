from catalog.interfaces.product_interface import IProduct
import inject
from discounts_app.interfaces.discounts_interface import IDiscounts



class LimitedProducts:
    _product: IProduct = inject.attr(IProduct)
    _discounts: IDiscounts = inject.attr(IDiscounts)

    def get_lp_with_product_discounts(self):

        all_lim_products = self._product.get_limited_products()

        product_discounts = self._discounts.get_all_active_product_discounts()

        for product in all_lim_products:
            for discount in product_discounts:
                if not product.id == discount.product.id:
                    all_lim_products.exclude(pk=product.id)
        print(all_lim_products)
        return all_lim_products
