from django import forms
from ..models import Seller


class SellerChangeForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ['logo', 'name']
        labels = {
            'name': 'Имя продавца',
        }
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'Profile-file form-input', 'required': False}),
        }
