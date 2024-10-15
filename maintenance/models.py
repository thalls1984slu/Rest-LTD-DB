from datetime import date
from django.db import models

from core.models import Job, Employee

# Create your models here.


class YearlySchedule(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    year = models.IntegerField(blank=True, null=True,default=0)
    amount=models.IntegerField(blank=True, null=True, default=0)
    scheduled_date = models.DateField(blank=True, null=True, default=date.today)
    completed_date=models.DateField(blank=True, null=True, default=date.today)
    employees = models.ManyToManyField(Employee, related_name='maintenance_jobs', blank=True)
    notes=models.TextField(blank=True, null=True, default='None')
    next_schdeuled_date=models.DateField(blank=True, null=True, default=date.today)
    completed=models.BooleanField(default=False, blank=True)
    

    def __str__(self):
        return f"{self.job.title}"