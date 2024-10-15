from django.shortcuts import render, get_object_or_404, redirect
from .models import Job, YearlySchedule
from .forms import YearlyScheduleForm

def job_schedule_view(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    schedules = YearlySchedule.objects.filter(job=job).order_by('year')
    return render(request, 'job_schedule.html', {'job': job, 'schedules': schedules})


def create_job_schedule(request):
    if request.method == 'POST':
        form =  YearlyScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            job=schedule.job
            schedule.save()
            return redirect('maintenance:job_schedule', job_id=job.id)
    else:
        form =  YearlyScheduleForm()

    return render(request, 'add_schedule.html', {'form': form})

def add_job_schedule(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    if request.method == 'POST':
        form = YearlyScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save(commit=False)
            schedule.job = job
            schedule.save()
            return redirect('maintenance:job_schedule', job_id=job.id)
    else:
        form = YearlyScheduleForm(initial={'job': job})
    return render(request, 'add_schedule.html', {'form': form, 'job': job})

def update_job_schedule(request, schedule_id):
    schedule = get_object_or_404(YearlySchedule, id=schedule_id)
    job = get_object_or_404(Job, id=schedule.job.id)   
    form = YearlyScheduleForm(instance=schedule)
    if request.method == 'POST':
        form = YearlyScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('maintenance:job_schedule', job_id=job.id)
    else:
        form = YearlyScheduleForm(instance=schedule)
    return render(request, 'add_schedule.html', {'form': form, 'job': job})

def delete_job_schedule(request, schedule_id):
    schedule = get_object_or_404(YearlySchedule, id=schedule_id)
    job = get_object_or_404(Job, id=schedule.job.id)    
    if request.method == 'POST':
        schedule.delete()
        return redirect('maintenance:job_schedule', job_id=job.id)
    return render(request, 'delete_job_schedule.html', {'schedule': schedule, 'job': job})