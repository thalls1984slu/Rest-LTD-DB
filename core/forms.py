from django import forms
from django.forms import FileInput, ModelForm, TextInput
from core.models import Job

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'  # Add other fields as needed
        
            
         

        
