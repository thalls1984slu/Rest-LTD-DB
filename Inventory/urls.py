# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('add/brand/', add_brand, name='add_brand'),
    path('add/battery/', add_battery, name='add_battery'),
    path('add/inverter/', add_inverter, name='add_inverter'),
    path('add/panel/', add_panel, name='add_panel'),
    path('add/brand/<int:pk>/', update_brand, name='update_brand'),
    path('add/battery/<int:pk>/', update_battery, name='update_battery'),
    path('add/panel/<int:pk>/', update_panel, name='update_panel'),
    path('add/inverter/<int:pk>/', update_inverter, name='update_inverter'),
    path('inventory', inventory_list, name='inventory_list'),
    path('delete/battery/<int:pk>/', delete_battery, name='delete_battery'),
    path('delete/panel/<int:pk>/', delete_panel, name='delete_panel'),
    path('delete/inverter/<int:pk>/', delete_inverter, name='delete_inverter'),
    path('delete/brand/<int:pk>/', delete_brand, name='delete_brand')
    # other URL patterns
]