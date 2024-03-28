from django import forms 
from django.core.exceptions import ValidationError
from .models import Character

class MyForms(forms.ModelForm):
    class Meta:
        model = Character
        fields = '__all__'