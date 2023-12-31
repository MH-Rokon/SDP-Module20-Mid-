from .models import Car
from django import forms

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'
       