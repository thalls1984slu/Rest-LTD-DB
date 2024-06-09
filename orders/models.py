from django.db import models
from datetime import date, timedelta
from django.utils.translation import gettext_lazy as _
from core.models import Job 
from inventory.models import *


    

class Order(models.Model):
    class OrderStatus(models.TextChoices):
        OPEN = 'OP',_('Open')
        CLOSED = 'CL', _('Closed')
    class Type(models.TextChoices):
        BATTERY = 'BA', _('Battery')
        INVERTER = 'IN', _('Inverter')
        PANEL = 'PN', _('Panel')
    brand_name=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name= "order_brands")
    type= models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.BATTERY,
    )
    model=models.CharField(max_length=255, default =0, blank=True, null=True)
    size = models.CharField(max_length=255, default =0, blank=True, null=True)
    quantity = models.IntegerField(default =0,blank=True, null=True)
    cost=models.IntegerField(default =0,blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name= "job",default=None,blank=True, null=True)
    notes=models.TextField(default=None,blank=True, null=True)
    order_date=models.DateField( default=date.today)
    due_date=models.DateField(default=None,blank=True, null=True)
    date_received=models.DateField(default=None,blank=True, null=True)
    order_status= models.CharField(
        max_length=2,
        choices=OrderStatus.choices,
        default=OrderStatus.OPEN,
    )
    def __str__(self):
        return self.brand_name.name+' '+self.model
    