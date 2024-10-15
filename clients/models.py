from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Community(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Communities'
        ordering = ('name',)

    def __str__(self):
        return self.name
    

class Account(models.Model):
    type = models.CharField(max_length=255)
    def __str__(self):
        return self.type

class Client(models.Model):
    class ClientStatus(models.TextChoices):
        NEW = 'NW', _('New')
        RECURRENT = 'RC', _('Recurrent')
        REFERRAL = 'RF', _('Referral')
        THIRD_PARTY = 'TP', _('Third Party')

    name = models.CharField(max_length=255)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    accountType = models.ForeignKey(Account, on_delete=models.CASCADE, default = 0)
    contact_email = models.CharField(max_length=255, default =0)
    contact_phone = models.CharField(max_length=255, default=0)
    billing_address = models.CharField(max_length=255, default=0)
    
    client_status = models.CharField(
        max_length=2,
        choices=ClientStatus.choices,
        default=ClientStatus.NEW,
    )
        

    # Add other fields for client details

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
