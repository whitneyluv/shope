from django import forms
from ..models import Seller


class SellerForm(forms.ModelForm):

    class Meta:
        model = Seller
        fields = ['logo', 'name', 'description']
        labels = {
            'name': 'Название компании',
            'description': 'Описание компании',
        }
        widgets = {
            'logo': forms.FileInput(attrs={'class': 'Profile-file form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-textarea'}),
        }
