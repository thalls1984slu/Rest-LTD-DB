from django.db import models

from clients.models import Client
from clients.models import Community
from django.utils.translation import gettext_lazy as _

# Create your models here.

class System(models.Model):
    title = models.CharField(max_length=255)
    cost = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    instock = models.BooleanField(default=False)
    

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    
class Payment(models.Model):
    type= models.CharField(max_length=255)

    class Meta:
        ordering = ('type',)
    
    def __str__(self):
        return self.type

class Picture(models.Model):
    picture = models.ImageField(upload_to='job_images/', blank=True, null=True)  

    def __str__(self):
        return self.picture.url
    
class Document(models.Model):
    document = models.FileField(upload_to='job_documents/', blank=True, null=True) 

    def __str__(self):
        return self.document.url



class Job(models.Model):

    class JobProgress(models.TextChoices):
        CONSULTATION = 'CS', _('Consultation')
        IN_PROGRESS = 'IP', _('In progress')
        CLOSED = 'CL', _('Closed')
    
    class JobRisk(models.TextChoices):
        HIGH = 'HI', _('High')
        MEDIUM = 'MI', _('Medium')
        LOW = 'LO', _('Low')
        
    title = models.CharField(max_length=255)
    job_progress = models.CharField(
        max_length=2,
        choices=JobProgress.choices,
        default=JobProgress.CONSULTATION,
    )   
    job_risk = models.CharField(
        max_length=2,
        choices=JobRisk.choices,
        default=JobRisk.LOW,
    ) 

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='jobs')
    location = models.ForeignKey(Community, on_delete=models.CASCADE)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    employees = models.ManyToManyField('Employee', related_name='jobs')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    duration = models.FloatField(default=0)
    documents = models.ManyToManyField(Document, blank=True, related_name="job_doc") 
    images = models.ManyToManyField(Picture, blank=True, related_name="job_img")
    display_image= models.ImageField(upload_to='job_images/', default = 'job_images/rest_logo.jpg', blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    # Add other fields for job details

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
    
class Employee(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    wage = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='employee_images/', default='employee_images/human_placeholder.png', blank=True, null=True)
    # Add other fields for employee details

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Compensation(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    daysWorked = models.DecimalField(max_digits=5, decimal_places=2)
    compensation = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('job',)

    def __str__(self):
        return self.job + self.employee
    


