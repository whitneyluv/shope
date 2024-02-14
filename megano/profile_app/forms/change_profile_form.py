from django import forms
from ..models import Profile


class ProfileForm(forms.ModelForm):

    avatar = forms.ImageField(widget=forms.FileInput())
    username = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Profile
        fields = "user", "avatar"

