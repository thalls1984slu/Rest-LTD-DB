# urls.py
from django.urls import path
from .views import *

app_name = 'orders'

urlpatterns = [
    path('add/', create_order, name='create_order'),
    path('delete/<int:pk>/', delete_order, name='delete_order'),
    path('update/<int:pk>/', update_order, name='update_order'),
    path('order_list/', order_list, name='order_list'),
    path('<int:pk>/', order_detail, name='order_detail'),
]