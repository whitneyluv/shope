import inject

from auth_app.interfaces.auth_interface import IAuth
from auth_app.repositories.auth_repositories import AuthRepository
from catalog.interfaces.catalog_interface import ICatalogRepository
from catalog.repositories.catalog_repositories import CatalogRepository

BINDS = (
    (IAuth, AuthRepository),
    (ICatalogRepository, CatalogRepository),
)


def config(binder):
    """Конфигуратор для inject."""
    for interface, implementation in BINDS:
        binder.bind(interface, implementation())


def configure_inject():
    """Конфигурирует зависимости для проекта."""
    inject.configure_once(config)
