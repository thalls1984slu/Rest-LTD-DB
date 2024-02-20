# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect

from clients.forms import ClientCreationForm

from core.filters import ClientFilter

from clients.models import Client


def detail(request, pk):
    client = get_object_or_404(Client, pk=pk)

    related_jobs = client.jobs.all()

    job_instance = client.jobs.first()

    context={'related_jobs':related_jobs, 'client':client}

    return render(request, 'client/detail.html', context) 


def create_client(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jobs:job_list')  # Redirect to the Job list page
    else:
        form = ClientCreationForm()

    return render(request, 'client/create_client.html', {'form': form})


def client_list(request):
    client_filter = ClientFilter(request.GET, queryset=Client.objects.all())
    form=client_filter.form
    clients = client_filter.qs
    context = {'clients': clients , 'form': form}
    return render(request, 'client/client_list.html', context)
   

def update_client(request, pk):
    client=Client.objects.get(id=pk)
    form = ClientCreationForm(instance=client)
    if request.method == 'POST':
        form = ClientCreationForm(request.POST, instance = client)
    context= {'form': form}
    if form.is_valid():
            form.save()
            return redirect('client:client_list')  # Redirect to the Client list page
    else:
        form = ClientCreationForm()

    return render(request, 'client/create_client.html', context)

def delete_client(request, pk):
    client=Client.objects.get(pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client:client_list') 
    
    context = {'item': client}
    return render(request, 'client/delete_client.html', context)