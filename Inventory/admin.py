from django.contrib import admin

from import_export import resources

from import_export.admin import ImportExportModelAdmin

from .models import Inverter, Battery, Panel , Brand 

class InverterResource(resources.ModelResource):

    class Meta:
        model = Inverter 
        exclude = ('id', ) 

class BatteryResource(resources.ModelResource):

    class Meta:
        model = Battery 
        exclude = ('id', )

class PanelResource(resources.ModelResource):

    class Meta:
        model = Panel  
        exclude = ('id', )

class BrandResource(resources.ModelResource):

    class Meta:
        model = Brand 
        exclude = ('id', ) 

# Register your models here.
class InverterAdmin(ImportExportModelAdmin):
    resource_classes = [InverterResource]
admin.site.register(Inverter, InverterAdmin)

class BatteryAdmin(ImportExportModelAdmin):
    resource_classes = [BatteryResource]
admin.site.register(Battery, BatteryAdmin)

class PanelAdmin(ImportExportModelAdmin):
    resource_classes = [PanelResource]
admin.site.register(Panel, PanelAdmin)

class BrandAdmin(ImportExportModelAdmin):
    resource_classes = [BrandResource]

admin.site.register(Brand, BrandAdmin)
