from django import forms
from ..models import Profile


class UserProfileChangeForm(forms.ModelForm):

    username = forms.CharField(label='ФИО', required=False)

    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'phone']
        labels = {
            'username': 'Имя пользователя',
            'phone': 'Телефон',
        }
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'Profile-file form-input'}),
        }
