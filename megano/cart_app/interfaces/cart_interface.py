from abc import abstractmethod, ABC

from auth_app.models.user import User
from cart_app.models import Cart


class ICart(ABC):
    """Интерфейс взаимодействия с данными модели Cart"""

    @abstractmethod
    def get_cart_by_user(self, user: User) -> Cart | None:
        """Получить экземпляр модели Cart"""
        pass

    @abstractmethod
    def save(self, model: Cart) -> None:
        """Сохранить экземпляр модели Cart"""
        pass
