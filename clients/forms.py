from django import forms
from django.forms import FileInput, ModelForm, TextInput
from core.models import Client

class ClientCreationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # Add other fields as needed