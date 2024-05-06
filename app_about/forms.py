from django import forms
from .models import AboutInfo
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Service


class AboutInfoForm(forms.ModelForm):
    class Meta:
        model = AboutInfo
        fields = ['description', 'image', 'birthday', 'website', 'phone', 'city', 'age', 'degree', 'email', 'freelance_available']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'image': forms.FileInput(),
        }

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    password = None  


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2') 




class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description'] 
