import django_filters

from .models import Employee, Job

from clients.models import Client

from inventory.models import Battery, Brand, Panel, Inverter

from orders.models import Order


class EmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields= {
            'name' : ['icontains'], 
            'title': ['icontains'], 
            'email': ['icontains'],
            'wage' : ['lt', 'gt']
            }
        
class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Job
        fields= {
            'title' : ['icontains'], 
            'location': ['exact'], 
            'job_progress' : ['exact'], 
            'system': ['exact'],
            'amount' : ['lt', 'gt']
            }
        
class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields= {
            'name' : ['icontains'], 
            'community': ['exact'], 
            'accountType': ['exact'],
            'client_status' : ['exact']
            }
 
class BatteryFilter(django_filters.FilterSet):
    class Meta:
        model = Battery
        fields= {
            'stock_status': ['exact'],
            'brand_name' : ['exact'], 
            'model': ['icontains'], 
            'size': ['icontains'], 
            'serial' : ['icontains'],
            'job' : ['exact'], 
            'in_use' : ['exact'],
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['brand_name'].queryset = Brand.objects.filter(battery_brand=True)

class PanelFilter(django_filters.FilterSet):
    class Meta:
        model = Panel
        fields= {
            'stock_status': ['exact'],
            'brand_name' : ['exact'], 
            'model': ['icontains'], 
            'size': ['icontains'], 
            'serial' : ['icontains'],
            'job' : ['exact'], 
            'in_use' : ['exact'],
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['brand_name'].queryset = Brand.objects.filter(panel_brand=True)

class InverterFilter(django_filters.FilterSet):
    class Meta:
        model = Inverter
        fields= {
            'stock_status': ['exact'],
            'grid_type': ['exact'],
            'brand_name' : ['exact'], 
            'model': ['icontains'], 
            'size': ['icontains'], 
            'serial' : ['icontains'],
            'job' : ['exact'], 
            'in_use' : ['exact'],
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['brand_name'].queryset = Brand.objects.filter(inverter_brand=True)


class BrandFilter(django_filters.FilterSet):
    class Meta:
        model = Brand
        fields= {
            'name': ['icontains'],
            'battery_brand': ['exact'],
            'inverter_brand' : ['exact'], 
            'panel_brand' : ['exact'], 
            }
        
class OrderFilter(django_filters.FilterSet):
    class Meta: 
        model = Order
        fields= { 
            'order_status': ['exact'],
            'job' : ['exact'], 
        
    

        }