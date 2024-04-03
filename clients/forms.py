from django import forms
from django.forms import FileInput, ModelForm, TextInput
from core.models import Client, Community

class ClientCreationForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # Add other fields as needed


class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = '__all__'  # Add other fields as needed