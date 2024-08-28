from django import forms
from django.forms import FileInput, ModelForm, TextInput
from core.models import Job, Employee

class JobCreationForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'  # Add other fields as needed
       
    def __init__(self, *args, **kwargs):
        super(JobCreationForm, self).__init__(*args, **kwargs)
        # Filter the employee queryset to only include current employees
        self.fields['employee'].queryset = Employee.objects.filter(employee_status=Employee.employee_status.CURRENT)
        
            
         

        
