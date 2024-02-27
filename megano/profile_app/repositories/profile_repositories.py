from beartype import beartype
from ..interfaces import IProfile
from ..models.profile import Profile
from typing import Optional


class ProfileRepository(IProfile):

    @beartype
    def save(self, model: Profile) -> None:
        """Сохранить профиль пользователя."""
        model.save()

    @beartype
    def get_profile_by_user_id(self, _user_id: int):
        """Получаем пользователя"""
        print(_user_id)
        print(Profile.objects.get(user_id=_user_id))
        return Profile.objects.get(user_id=_user_id)

    @beartype
    def delete_profile_by_user_id(self, _user_id: int):
        """Удаление профиля пользователя по user_id"""
        profile = Profile.objects.get(user_id=_user_id)
        profile.delete()
