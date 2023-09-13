from django import forms
from .models import Eventapp

class EventappForm(forms.ModelForm):
    class Meta:
        model = Eventapp
        fields = ['full_name','email','phone']
