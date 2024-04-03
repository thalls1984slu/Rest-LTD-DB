from django.contrib import admin

# Register your models here.
from .models import Inverter, Battery, Panel , Brand 
admin.site.register(Inverter)
admin.site.register(Battery)
admin.site.register(Panel)
admin.site.register(Brand)
