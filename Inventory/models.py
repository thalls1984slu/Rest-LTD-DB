from django.db import models
from django.forms import ValidationError
from django.utils.translation import gettext_lazy as _
from core.models import Job 

# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=255, default =0, blank=True, null=True)
    battery_brand = models.BooleanField(default=False)
    inverter_brand = models.BooleanField(default=False)
    panel_brand = models.BooleanField(default=False)
    def __str__(self):
        return self.name


class Battery(models.Model):
    class StockStatus(models.TextChoices):
        NEW = 'NW',_('New')
        USED = 'UD', _('Used')
    
    stock_status = models.CharField(
        max_length=2,
        choices=StockStatus.choices,
        default=StockStatus.NEW,
    )
    brand_name=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name= "battery_brands") 
    model=models.CharField(max_length=255, default =0, blank=True, null=True)
    size = models.CharField(max_length=255, default =0, blank=True, null=True)
    serial= models.CharField(max_length=255, default =0, blank=True, null=True, unique=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name= "battery_job",default=None,blank=True, null=True)
    assigned=models.BooleanField(default=False, blank=True)
    in_use=models.BooleanField(default=False, blank=True)
    def clean(self):
        super().clean()

        # Ensure serial is unique
        if Battery.objects.exclude(pk=self.pk).filter(serial=self.serial).exists():
            raise ValidationError({'serial': 'Serial number must be unique.'})

        # For updates, ensure serial doesn't change to an existing one
        if self.pk:
            original = Battery.objects.get(pk=self.pk)
            if original.serial != self.serial and Battery.objects.filter(serial=self.serial).exists():
                raise ValidationError({'serial': 'Cannot change to an existing serial number.'})
    def save(self, *args, **kwargs):
        if self.job:
            if self.job.job_progress == 'In progress':
                self.assigned = True
            else: 
                if self.job.job_progress == 'Finished':
                    self.in_use = True
        super().save(*args, **kwargs)
    def __str__(self):
        return  self.brand_name.name +' '+ self.model+' '+ self.size

class Panel(models.Model):
    class StockStatus(models.TextChoices):
        NEW = 'NW',_('New')
        USED = 'UD', _('Used')
    stock_status = models.CharField(
        max_length=2,
        choices=StockStatus.choices,
        default=StockStatus.NEW,
    )
    brand_name=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name= "panel_brands") 
    model=models.CharField(max_length=255, default =0, blank=True, null=True)
    size = models.CharField(max_length=255, default =0, blank=True, null=True, unique=True)
    serial= models.CharField(max_length=255, default =0, blank=True, null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name= "panel_job",default=None,blank=True,null=True)
    assigned=models.BooleanField(default=False, blank=True)
    in_use=models.BooleanField(default=False, blank=True)
    def clean(self):
        super().clean()

        # Ensure serial is unique
        if Panel.objects.exclude(pk=self.pk).filter(serial=self.serial).exists():
            raise ValidationError({'serial': 'Serial number must be unique.'})

        # For updates, ensure serial doesn't change to an existing one
        if self.pk:
            original = Panel.objects.get(pk=self.pk)
            if original.serial != self.serial and Panel.objects.filter(serial=self.serial).exists():
                raise ValidationError({'serial': 'Cannot change to an existing serial number.'})
    def save(self, *args, **kwargs):
        if self.job:
            if self.job.job_progress == 'In progress':
                self.assigned = True
            else: 
                if self.job.job_progress == 'Finished':
                    self.in_use = True
        super().save(*args, **kwargs)
    def __str__(self):
        return self.brand_name.name +' '+ self.model+' '+ self.size

class Inverter(models.Model):
    class StockStatus(models.TextChoices):
        NEW = 'NW',_('New')
        USED = 'UD', _('Used')
    class GridType(models.TextChoices):
        ONGRID = 'NG',_('On Grid')
        OFFGRID = 'OG', _('Off Grid')
        HYBRID = 'HB', _('Hybrid')
    stock_status = models.CharField(
        max_length=2,
        choices=StockStatus.choices,
        default=StockStatus.NEW,
    )
    grid_type = models.CharField(
        max_length=2,
        choices=GridType.choices,
        default=GridType.ONGRID,
    )
    brand_name=models.ForeignKey(Brand, on_delete=models.CASCADE, related_name= "inverter_brands") 
    model=models.CharField(max_length=255, default =0, blank=True, null=True)
    size = models.CharField(max_length=255, default =0, blank=True, null=True)
    serial= models.CharField(max_length=255, default =0, blank=True, null=True, unique=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name= "inverter_job",default=None,blank=True, null=True)
    assigned=models.BooleanField(default=False, blank=True)
    in_use=models.BooleanField(default=False, blank=True)
    def clean(self):
        super().clean()

        # Ensure serial is unique
        if Inverter.objects.exclude(pk=self.pk).filter(serial=self.serial).exists():
            raise ValidationError({'serial': 'Serial number must be unique.'})

        # For updates, ensure serial doesn't change to an existing one
        if self.pk:
            original = Inverter.objects.get(pk=self.pk)
            if original.serial != self.serial and Inverter.objects.filter(serial=self.serial).exists():
                raise ValidationError({'serial': 'Cannot change to an existing serial number.'})
    def save(self, *args, **kwargs):
        if self.job:
            if self.job.job_progress == 'In progress':
                self.assigned = True
            else: 
                if self.job.job_progress == 'Finished':
                    self.in_use = True
        super().save(*args, **kwargs)
    def __str__(self):
        return self.brand_name.name +' '+ self.model+' '+ self.size
    
