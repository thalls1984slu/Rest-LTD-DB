from django.urls import path

from maintenance.views import *  

# urls.py

app_name ='maintenance'

urlpatterns = [
    path('view/<int:job_id>/', job_schedule_view, name='job_schedule'),
    path('add/<int:job_id>', add_job_schedule, name='add_schedule'),
    path('update/<int:schedule_id>/', update_job_schedule, name='update_schedule'),
    path('delete/<int:schedule_id>/', delete_job_schedule, name='delete_schedule'),
   # path('list/', job_schedule_list, name='job_schedule_list'),

]