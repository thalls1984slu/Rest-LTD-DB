from django.contrib import admin

# Register your models here.
from .models import System
admin.site.register(System)

from .models import Payment
admin.site.register(Payment)

from .models import Employee
admin.site.register(Employee)

from .models import Job
admin.site.register(Job)

from .models import Compensation
admin.site.register(Compensation)

from .models import Picture
admin.site.register(Picture)

from .models import Document
admin.site.register(Document)


