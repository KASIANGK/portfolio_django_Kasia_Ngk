from django import forms
from .models import AboutInfo

from django import forms
from .models import AboutInfo

class AboutInfoForm(forms.ModelForm):
    class Meta:
        model = AboutInfo
        fields = ['description',  'image', 'birthday', 'website', 'phone', 'city', 'age', 'degree', 'email', 'freelance_available']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(),

        }