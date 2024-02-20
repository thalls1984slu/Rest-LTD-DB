from django.urls import path

from . import views

app_name = 'client'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create_client, name='create_client'),
    path('update/<int:pk>', views.update_client, name='update_client'),
    path('client_list/', views.client_list, name='client_list'),
    path('delete/<int:pk>', views.delete_client, name='delete_client'),


]