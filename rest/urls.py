"""
URL configuration for rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import statistics
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.views import index
from members.views import login_user, logout_user
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name ='index'),
    path('clients/', include('clients.urls')),
    path('employees/',include('employees.urls'), name ='employees'),
    path('jobs/', include('core.urls'), name ='jobs'),  
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('inventory/', include('inventory.urls'), name ='inventory'),   
    path('orders/', include('orders.urls'), name ='orders'), 
    path('maintenance/', include('maintenance.urls'), name ='maintenance'),
    

   
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)