from django import forms
from .models import Testimonial

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['content', 'author', 'designation', 'image'] 
        widgets = {
            'image': forms.FileInput()
        }