from django import forms
from django.forms import FileInput, ModelForm, TextInput
from .models import Battery, Panel, Inverter, Brand
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit, Div

class BatteryForm(ModelForm):
    class Meta:
        model = Battery
        fields = '__all__' 
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand_name'].queryset = Brand.objects.filter(battery_brand=True)

class PanelForm(ModelForm):
    class Meta:
        model = Panel
        fields = '__all__'  # Add other fields as needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand_name'].queryset = Brand.objects.filter(panel_brand=True)
   
    

class InverterForm(ModelForm):
    class Meta:
        model = Inverter
        fields = '__all__'  # Add other fields as needed
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['brand_name'].queryset = Brand.objects.filter(inverter_brand=True)


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'  # Add other fields as needed
   