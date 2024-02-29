from abc import abstractmethod, ABC

from profile_app.models.seller import Seller


class ISeller(ABC):
    """Интерфейс взаимодействия с данными модели Seller"""

    @abstractmethod
    def get_seller(self, pk: int) -> Seller | None:
        """Получить экземпляр модели Seller"""
        pass
