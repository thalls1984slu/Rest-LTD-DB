# employees/forms.py
from django import forms
from django.forms import FileInput, ModelForm, TextInput
from core.models import Employee

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'title', 'email','wage','images' ]  # Add other fields as needed
        images = forms.ImageField() 
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; border: 2px solid red;  border-radius: 5px;',
                'placeholder': 'Name'
                }),
            'title': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Title'
                }),
            'email': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'wage': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Wage'
                }),
            'images': TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Images'
                }),
            

        }

class EmployeeCreationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_status','name', 'title','dob','address', 'email','wage','images' ]  # Add other fields as needed
        images = forms.ImageField() 
        widgets = {
            'current': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'margin-top: 10px; margin-bottom: 10px;',
                'labels': 'Current Employee?'
                }),
            'name': TextInput(attrs={
                'class': "form-control",
                'style': 'mt-5 max-width: 300px; ',
                'placeholder': 'Name'
                }),
            'title': TextInput(attrs={
                'class': "form-control", 
                'style': 'mt-5 max-width: 300px;',
                'placeholder': 'Title'
                }),
            'email': TextInput(attrs={
                'class': "form-control", 
                'style': 'mt-5 max-width: 300px;',
                'placeholder': 'Email'
                }),
            'wage': TextInput(attrs={
                'class': "form-control", 
                'style': 'mt-5 max-width: 300px;',
                'placeholder': 'Wage'
                }),
            'images': FileInput(attrs={
                'id' : 'image_field' , 
                'style': 'height: 50px ;  color: white; '
                    })
            
            

        }

