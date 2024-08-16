from django.urls import path

from core import views



app_name = 'jobs'

urlpatterns = [
    path('<int:pk>/',  views.job_detail, name='jobs'),
    path('create/', views.create_job, name='create_job'),
    path('update/<int:pk>', views.update_job, name='update_job'),
    path('job_list/', views.job_list, name='job_list'),
    path('delete/<int:pk>', views.delete_job, name='delete_job'),
    #path('schedule/view/<int:job_id>', views.job_schedule_view, name='job_schedule'),
    #path('schedule/add/<int:job_id>', views.add_job_schedule, name='add_schedule'),
    #path('schedule/update/<int:pk>', views.update_schedule, name='update_schedule'),
    #path('schedule/delete/<int:pk>', views.delete_schedule, name='delete_schedule'),
     
     
]


