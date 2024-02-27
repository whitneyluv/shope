from django import forms
from ..models import Profile


class UserProfileChangeForm(forms.ModelForm):

    username = forms.CharField(max_length=150, label='ФИО', required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'phone']
        labels = {
            'username': 'Имя пользователя',
            'phone': 'Телефон',
        }
        widgets = {
            'avatar': forms.FileInput(attrs={'class': 'Profile-file form-input'}),
        }

    def save(self, commit=True):
        profile = super().save(commit=False)
        username = self.cleaned_data.get('username')
        if username:
            profile.user.username = username
            profile.user.save()
        profile.avatar = self.cleaned_data.get('avatar')
        profile.phone = self.cleaned_data.get('phone')
        if commit:
            profile.save()
        return profile
