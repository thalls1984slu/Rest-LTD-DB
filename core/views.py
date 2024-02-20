from django.shortcuts import render, get_object_or_404, redirect

from core.models import Job, Employee 

from clients.models import Client
from core.forms import JobCreationForm 

from core.filters import JobFilter 
# Create your views here.

#listing of the 5 most recent objects on the homepage
def index(request):
    jobs = Job.objects.all().order_by('-id')[:5]
    employees = Employee.objects.all().order_by('-id')[:5]
    clients = Client.objects.all().order_by('-id')[:5]
    all_jobs=Job.objects.all()
    all_employees=Employee.objects.all()
    all_clients = Client.objects.all()
    context ={'jobs':jobs, 'employees':employees, 'clients':clients, 'all_clients':all_clients, 'all_jobs':all_jobs, 'all_employees':all_employees}

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

def inventory(request):
    return render(request, 'core/inventory.html')


# Job Details View
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    employees = job.employees.all()
    
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

    return render(request, 'core/job_detail.html', {'job':job, 'employees':employees})


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