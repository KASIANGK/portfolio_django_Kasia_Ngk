from django import forms
from .models import Skill



class AddSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'skill '})
        self.fields['level'].widget.attrs.update({'class': 'form-control', 'placeholder': 'niveau de maîtrise (0-100)'})



