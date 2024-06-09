from django import forms
from django.forms import FileInput, ModelForm, TextInput
from .models import YearlySchedule

class YearlyScheduleForm(ModelForm):
    class Meta:
        model = YearlySchedule
        fields = '__all__'  # Add other fields as needed
        widgets = {
            'scheduled_date': forms.DateInput(attrs={'class': 'datepicker'}),
            'completed_date': forms.DateInput(attrs={'class': 'datepicker'}),
        }