import inject

from megano.auth_app.interfaces.auth_interface import IAuth
from megano.auth_app.repositories.auth_repositories import AuthRepository
from megano.catalog.interfaces.catalog_interface import ICatalogRepository
from megano.catalog.repositories.catalog_repositories import CatalogReposito
from megano.profile_app.interfaces import IProfile
from megano.profile_app.repositories import ProfileRepository
from megano.coreapp.interfaces.core_interface import ICore
from megano.coreapp.repositories.core_repositories import CoreRepository
from megano.discounts_app.interfaces.discounts_interface import IDiscounts
from megano.discounts_app.repositories.discounts_repositories import DiscountsRepository
from megano.order_app.interface.order_interface import IOrder
from megano.order_app.repositeries.order_repositories import OrderRepository

BINDS = (
    (IAuth, AuthRepository),
    (ICatalogRepository, CatalogRepository),
    (IProfile, ProfileRepository),
    (ICore, CoreRepository),
    (IDiscounts, DiscountsRepository),
    (IOrder, OrderRepository)

)


def config(binder):
    """Конфигуратор для inject."""
    for interface, implementation in BINDS:
        binder.bind(interface, implementation())


def configure_inject():
    """Конфигурирует зависимости для проекта."""
    inject.configure_once(config)
