from django.urls import path

from core import views



app_name = 'jobs'

urlpatterns = [
    path('<int:pk>/',  views.job_detail, name='jobs'),
    path('create/', views.create_job, name='create_job'),
    path('update/<int:pk>', views.update_job, name='update_job'),
    path('job_list/', views.job_list, name='job_list'),
    path('delete/<int:pk>', views.delete_job, name='delete_job'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
]


