from django import forms
from ..models import Profile


class ProfileChangeForm(forms.ModelForm):

    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'Profile-file form-input'}))
    username = forms.CharField(max_length=150, label='Имя пользователя')
    email = forms.EmailField()
    phone = forms.CharField(label='Телефон', widget=forms.NumberInput(attrs={'type': 'tel', 'class': 'data-tel-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Пароль')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Подтверждение пароля')

    class Meta:
        model = Profile
        fields = 'avatar', 'username', 'email', 'phone', 'password1', 'password2'
