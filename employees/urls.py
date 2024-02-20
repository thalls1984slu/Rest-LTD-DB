from django.urls import path

from . import views

from .views import *

app_name = 'employees'

urlpatterns = [
     path('<int:pk>/', views.detail, name='detail'),
     path('update/<int:pk>/', update_employee, name='update_employee'),
     path('create/', create_employee, name='create_employee'),
     path('employee_list/', employee_list, name='employee_list'),
     path('delete/<int:pk>/', delete_employee, name='delete_employee'),
]