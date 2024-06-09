from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from django.db.models import F, ExpressionWrapper, DecimalField

from core.models import Job, Employee 

from clients.models import Client

from inventory.models import Battery, Panel, Inverter

from core.forms import JobCreationForm 

from core.filters import JobFilter
from maintenance.models import YearlySchedule 
# Create your views here.

#listing of the 5 most recent objects on the homepage

@login_required(login_url='login')
def index(request):
    jobs = Job.objects.all().order_by('-id')[:5]
    employees = Employee.objects.all().order_by('-id')[:5]
    clients = Client.objects.all().order_by('-id')[:5]
    schedule = YearlySchedule.objects.filter(completed=False).order_by('scheduled_date')[:5]
    financial_records = Job.objects.annotate(
        profitability=ExpressionWrapper(
            F('amount_actual') - F('amount'),
            output_field=DecimalField()
        )
    ).order_by('-profitability')[:5]
    low_financial_records = Job.objects.annotate(
        profitability=ExpressionWrapper(
            F('amount_actual') - F('amount'),
            output_field=DecimalField()
        )
    ).order_by('profitability')[:5]

    context ={'schedule':schedule,'jobs':jobs, 'employees':employees, 'clients':clients,'financial_records':financial_records, 'low_financial_records':low_financial_records}

    return render(request, 'core/index.html',context)

def login_page(request):
    context = {}
    return render(request, 'core/login.html', context)

def logout_page(request):
    context = {}
    return render(request, 'core/loout.html', context)

#def client(request):
#   return render(request, 'core/client.html')

def employee(request):
    return render(request, 'core/employee.html')


# Job Details View
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    employees = job.employees.all()
    batteries = Battery.objects.filter(job_id=pk)
    panels = Panel.objects.filter(job_id=pk)
    inverters = Inverter.objects.filter(job_id=pk)
    
    #job_instance = employee.jobs.first()

    #if job_instance:
    #    total_job_time = sum(job.duration for job in related_jobs)
    #    job_payments = [(job.title, int(job.duration) * employee.wage) for job in related_jobs]
   # else:
    #    total_job_time = 0
    #    job_payments = [('no jobs', total_job_time) for job in related_jobs]

   # job_payment= employee.wage

    #amount_paid = float(employee.wage) * total_job_time

    #job_instance = client.jobs.first()

   

    #return render(request, 'client/detail.html', {'related_jobs':related_jobs,'job_cost':job_cost, 'client':client}) 

    context = { 'job':job, 
               'employees':employees,
               'batteries': batteries,
                'panels': panels,
                'inverters': inverters}
    return render(request, 'core/job_detail.html', context)


def create_job(request):
    if request.method == 'POST':
        form = JobCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobs:job_list')  # Redirect to the Job list page
    else:
        form = JobCreationForm()

    return render(request, 'core/create_job.html', {'form': form})


def job_list(request):
    job_filter = JobFilter(request.GET, queryset=Job.objects.all())
    form=job_filter.form
    jobs = job_filter.qs
    context = {'jobs': jobs, 'form': form}
    return render(request, 'core/job_list.html', context)
   

def update_job(request, pk):
    job=Job.objects.get(id=pk)
    form = JobCreationForm(instance=job)
    if request.method == 'POST':
        form = JobCreationForm(request.POST, instance = job)
    context= {'form': form}
    if form.is_valid():
            form.save()
            return redirect('jobs:job_list')  # Redirect to the Job list page
    else:
        form = JobCreationForm()

    return render(request, 'core/create_job.html', context)
    
def delete_job(request, pk):
    job=Job.objects.get(pk=pk)
    if request.method == 'POST':
        job.delete()
        return redirect('jobs:job_list') 
    
    context = {'item': job}
    return render(request, 'core/job_delete.html', context)