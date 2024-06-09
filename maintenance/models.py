from django.db import models

from core.models import Job

# Create your models here.


class YearlySchedule(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    year = models.IntegerField()
    scheduled_date = models.DateField()
    completed_date=models.DateField(blank=True, null=True, default=None)
    notes=models.TextField(blank=True, null=True, default='None')
    completed=models.BooleanField(default=False, blank=True)
    

    def __str__(self):
        return f"{self.job.title} - {self.year}"