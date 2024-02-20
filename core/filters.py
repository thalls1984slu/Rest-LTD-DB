import django_filters

from .models import Employee, Job

from Inventory.models import Inventory

from clients.models import Client


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
        
class InventoryFilter(django_filters.FilterSet):
    class Meta:
        model = Inventory
        fields= {
            'stock_type' : ['exact'], 
            'stock_status': ['exact'], 
            'barcode' : ['icontains'], 
            'brand': ['icontains'],
            'cost' : ['lt', 'gt']
            }