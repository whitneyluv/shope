from abc import abstractmethod, ABC

from cart_app.models import CartItem


class ICartItem(ABC):
    """Интерфейс взаимодействия с данными модели CartItem"""

    @abstractmethod
    def save(self, model: CartItem) -> None:
        """Сохранить экземпляр модели CartItem"""
        pass
