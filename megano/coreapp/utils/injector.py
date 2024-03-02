import inject

from auth_app.interfaces.auth_interface import IAuth
from auth_app.repositories.auth_repositories import AuthRepository
from catalog.interfaces.catalog_interface import ICatalogRepository
from catalog.repositories.catalog_repositories import CatalogRepository
from profile_app.interfaces import IProfile
from profile_app.repositories import ProfileRepository
from coreapp.interfaces.core_interface import ICore
from coreapp.repositories.core_repositories import CoreRepository
from discounts_app.interfaces.discounts_interface import IDiscounts
from discounts_app.repositories.discounts_repositories import DiscountsRepository

BINDS = (
    (IAuth, AuthRepository),
    (ICatalogRepository, CatalogRepository),
    (IProfile, ProfileRepository),
    (ICore, CoreRepository),
    (IDiscounts, DiscountsRepository),
)

def config(binder):
    """Конфигуратор для inject."""
    for interface, implementation in BINDS:
        binder.bind(interface, implementation())

def configure_inject():
    """Конфигурирует зависимости для проекта."""
    inject.configure_once(config)
