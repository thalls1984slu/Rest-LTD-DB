from django.urls import path

from . import views

app_name = 'inventory'

urlpatterns = [
    path('<int:pk>/',  views.inventory_detail, name='inventory'),
    path('create/', views.create_inventory, name='create_inventory'),
    path('update/<int:pk>', views.update_inventory, name='update_inventory'),
    path('inventory_list/', views.inventory_list, name='inventory_list'),
    path('delete_inventory/<str:pk>', views.delete_inventory, name='delete_inventory'),

]