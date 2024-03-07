from abc import abstractmethod, ABC

from profile_app.models.seller import Seller
from auth_app.models import User


class ISeller(ABC):
    """Интерфейс взаимодействия с данными модели Seller"""

    @abstractmethod
    def get_seller(self, pk: int) -> Seller | None:
        """Получить экземпляр модели Seller"""
        pass

    @abstractmethod
    def get_seller_by_user(self, user: User) -> Seller | None:
        """Получить экземпляр модели Seller связанный с экземпляром модели User"""
        pass
