import inject
from profile_app.interfaces import ISeller
from catalog.interfaces import IProduct
from .dto import Product, Seller


class FillingSeller:
    """
    Модель для заполнения данными DTO модели Seller
    """
    _seller: ISeller = inject.attr(ISeller)

    def filling_from_session(self, seller_id: int):
        """
            Функция заполнения всей информации для модели выгружая информацию из request.session
        """
        seller = self._seller.get_seller(seller_id)
        return Seller(
            pk=seller.pk,
            name=seller.name
        )

    def filling_from_db(self, seller):
        """
            Функция заполнения всей информации для модели выгружая информацию из базы данных
        """
        return Seller(
            pk=seller.pk,
            name=seller.name
        )


class FillingProduct:
    """
        Модель для заполнения данными DTO модели Product
    """
    _product: IProduct = inject.attr(IProduct)

    def filling_from_session(self, product_id: int):
        """
        Функция заполнения всей информации для модели выгружая информацию из request.session
        """

        product = self._product.get_product(product_id)

        return Product(
            pk=product.pk,
            title=product.title,
            description=product.description,
            image=product.product_images.first().image.url
        )

    def filling_from_db(self, product):
        """
            Функция заполнения всей информации для модели выгружая информацию из базы данных
        """

        return Product(
            pk=product.pk,
            title=product.title,
            description=product.description,
            image=product.product_images.first().image.url
        )