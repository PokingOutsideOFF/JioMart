from django.core import validators
from django import forms
from .models import brands

class brandsForm(forms.ModelForm):
    class Meta:
        model = brands
        fields = '__all__'