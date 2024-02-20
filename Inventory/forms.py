from django import forms
from django.forms import FileInput, ModelForm, TextInput
from .models import Inventory

class InventoryCreationForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'  # Add other fields as needed   