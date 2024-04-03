from django import forms
from .models import FeedbackForm

class Form(forms.ModelForm) : 
    class Meta :
        model = FeedbackForm
        fields = ['name', 'place', 'message']


