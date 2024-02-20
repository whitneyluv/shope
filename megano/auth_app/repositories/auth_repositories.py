from beartype import beartype
from auth_app.interfaces.auth_interface import IAuth
from auth_app.models.user import User
from django.core.exceptions import ObjectDoesNotExist
from typing import Optional
from datetime import date, timedelta
from ..utils import get_activation_key


class AuthRepository(IAuth):

    @beartype
    def save(self, model: User) -> None:
        model.save()

    @beartype
    def get_user_by_email(self, _email: str) -> Optional[User]:
        """Получаем пользователя"""
        try:
            return User.objects.get(email=_email)
        except ObjectDoesNotExist:
            return None

    @beartype
    def get_user(self, model: User) -> User:
        """Получаем пользователя"""
        user = model
        return user

    @beartype
    def delete_user_by_email(self, _email: str) -> None:
        """Удаляем пользователя"""
        user = self.get_user_by_email(_email)
        if user:
            user.delete()

    @beartype
    def get_user_by_activation_key(self, _activation_key: str) -> Optional[User]:
        """Получаем пользователя по активационному ключу"""
        try:
            return User.objects.get(activation_key=_activation_key)
        except ObjectDoesNotExist:
            return None

    @beartype
    def set_user_is_active(self, model: User, value: bool) -> None:
        """Установить значение параметра is_active пользователя"""
        model.is_active = value
        self.save(model)

    @beartype
    def set_activation_key(self, model: User):
        """Установить значение параметра activation_key пользователя"""
        model.activation_key = get_activation_key(model.email)
        self.save(model)

    @beartype
    def set_activation_key_will_expires(self, model: User):
        """Установить значение параметра activation_key_will_expires пользователя"""
        model.activation_key_will_expires = date.today() + timedelta(2)
        self.save(model)
