from django import forms
from django.forms import FileInput, ModelForm, TextInput
from .models import Order

class OrderCreationForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # Add other fields as needed
        widgets = {
            'order_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'due_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'date_received': forms.DateInput(attrs={'class': 'datepicker'}),
        
        }