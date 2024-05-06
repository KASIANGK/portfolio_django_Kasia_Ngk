from django import forms
from .models import PortfolioItem

class PortfolioForm(forms.ModelForm):
    class Meta:
        model = PortfolioItem
        fields = ['title', 'filter', 'description', 'image']
        widgets = {
            'image' : forms.FileInput()
        }
