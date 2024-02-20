from abc import abstractmethod
from coreapp.models.banner import Banner


class ICore:

    @abstractmethod
    def get_banners(self, model: Banner):
        """Получить все активные баннеры"""
        pass
