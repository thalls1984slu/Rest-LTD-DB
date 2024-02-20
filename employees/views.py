from django.shortcuts import render, get_object_or_404, redirect

from employees.forms import EmployeeCreationForm

from core.filters import EmployeeFilter

# Create your views here.
from core.models import Employee , Job

# Employee Details View
def detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    related_jobs = employee.jobs.all()

    job_instance = employee.jobs.first()

    if job_instance:
        total_job_time = sum(job.duration for job in related_jobs)
        job_payments = [(job.title, int(job.duration) * employee.wage) for job in related_jobs]
    else:
        total_job_time = 0
        job_payments = [('no jobs', total_job_time) for job in related_jobs]

   # job_payment= employee.wage

    amount_paid = float(employee.wage) * total_job_time

    #job_instance = client.jobs.first()

   

    #return render(request, 'client/detail.html', {'related_jobs':related_jobs,'job_cost':job_cost, 'client':client}) 

    return render(request, 'core/employee_detail.html', {'employee':employee, 'related_jobs':related_jobs, 'amount_paid':amount_paid, 'job_payments':job_payments})


# employees/views.py



def employee_list(request):
    employee_filter = EmployeeFilter(request.GET, queryset=Employee.objects.all())
    form=employee_filter.form
    employees = employee_filter.qs
    return render(request, 'employees/employee_list.html', {'employees': employees, 'form': form})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees:employee_list')  # Redirect to the employee list page
    else:
        form = EmployeeCreationForm()

    return render(request, 'employees/create_employee.html', {'form': form})


def update_employee(request, pk):
    job=Employee.objects.get(pk=pk)
    form = EmployeeCreationForm(instance=job)
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST, request.FILES, instance=job)
    context= {'form': form}
    if form.is_valid():
            form.save()
            return redirect('employees:employee_list')  # Redirect to the employee list page
    else:
        form = EmployeeCreationForm()
    
    return render(request, 'employees/create_employee.html', context)


def delete_employee(request, pk):
    employee=Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employees:employee_list') 
    
    context = {'item': employee}
    return render(request, 'employees/delete_employee.html', context)