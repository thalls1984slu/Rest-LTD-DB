from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Inventory(models.Model):

    class StockType(models.TextChoices):
        PANEL = 'PN', _('Panel')
        INVERTER = 'IN', _('Inverter')
        BATTERY = 'BA', _('Battery')

    class StockStatus(models.TextChoices):
        NEW = 'NW',_('New')
        USED = 'UD', _('Used')
        
    stock_type = models.CharField(
        max_length=2,
        choices=StockType.choices,
        default=StockType.PANEL,
    )

    stock_status = models.CharField(
        max_length=2,
        choices=StockStatus.choices,
        default=StockStatus.NEW,
    )

    barcode = models.CharField(max_length=255, default =0 , blank=True, null=True)
    brand = models.CharField(max_length=255, default =0, blank=True, null=True)
    cost = models.CharField(max_length=255, default =0, blank=True, null=True)
    location = models.CharField(max_length=255, default =0, blank=True, null=True)
     
    class Meta:
        ordering = ('stock_type',)

    def __str__(self):
        return self.brand + self.stock_type

