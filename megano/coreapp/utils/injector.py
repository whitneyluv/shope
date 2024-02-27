import inject

from auth_app.interfaces.auth_interface import IAuth
from auth_app.repositories.auth_repositories import AuthRepository
from profile_app.interfaces import IProfile
from profile_app.repositories import ProfileRepository
from coreapp.interfaces.core_interface import ICore
from coreapp.repositories.core_repositories import CoreRepository

BINDS = (
    (IAuth, AuthRepository),
    (IProfile, ProfileRepository),
    (ICore, CoreRepository),

)


def config(binder):
    """Конфигуратор для inject."""
    for interface, implementation in BINDS:
        binder.bind(interface, implementation())


def configure_inject():
    """Конфигурирует зависимости для проекта."""
    inject.configure_once(config)
