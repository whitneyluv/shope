import inject

from shope.megano.auth_app.interfaces.auth_interface import IAuth
from shope.megano.auth_app.repositories.auth_repositories import AuthRepository

BINDS = (
    (IAuth, AuthRepository),

)


def config(binder):
    """Конфигуратор для inject."""
    for interface, implementation in BINDS:
        binder.bind(interface, implementation())


def configure_inject():
    """Конфигурирует зависимости для проекта."""
    inject.configure_once(config)
