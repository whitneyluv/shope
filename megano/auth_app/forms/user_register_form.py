import hashlib
import random
from django.contrib.auth.forms import UserCreationForm
from auth_app.models.user import User
from django.utils.translation import gettext_lazy as _
from django import forms


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации нового пользователя
    """

    error_messages = {
        "password_mismatch": _("Пароли не совпадают! Введите пароль заново"),
    }

    # username = forms.CharField(
    #     label='Имя пользователя',
    #     widget=forms.TextInput(
    #         attrs={'placeholder': 'Введите имя пользователя'}
    #     )
    # )
    email = forms.EmailField(
        label='Адрес эл.почты',
        widget=forms.EmailInput(
            attrs={'placeholder': 'Введите адрес эл.почты'}
        )
    )
    # middle_name = forms.CharField(
    #     label='Ваше имя',
    #     widget=forms.TextInput(
    #         attrs={'placeholder': 'Введите ваше имя'}
    #     )
    # )
    password1 = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Введите пароль'}
        )
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Повторите пароль'}
        )
    )

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    # def __init__(self, *args, **kwargs):
    #     super(UserRegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs({'placeholder': 'Введите имя пользователя'})
    #     self.fields['email'].widget.attrs['placeholder'] = 'Введите адрес эл.почты'
    #     self.fields['middle_name'].widget.attrs['placeholder'] = 'Введите имя'
    #     self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
    #     self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user
