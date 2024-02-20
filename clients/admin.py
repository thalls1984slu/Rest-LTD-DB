from django.contrib import admin

# Register your models here.
from .models import Client
admin.site.register(Client)

from .models import Community
admin.site.register(Community)

from .models import District
admin.site.register(District)


from .models import Account
admin.site.register(Account)