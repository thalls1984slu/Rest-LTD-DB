# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect

from .models import Inventory

from .forms import  InventoryCreationForm

from core.filters import  InventoryFilter



def inventory_detail(request, pk):
    inventory= get_object_or_404(Inventory, pk=pk)
    context = {'inventory':inventory}
    return render(request, 'inventory_detail.html', context)

  
   
def create_inventory(request):
    if request.method == 'POST':
        form = InventoryCreationForm(request.POST)
   
        if form.is_valid():
            form.save()
            return redirect('inventory:inventory_list')  # Redirect to the inventory list page
    else:
        form = InventoryCreationForm()
    
    context= {'form': form}

    return render(request, 'create_inventory.html', context)


def inventory_list(request):
    inventory_filter = InventoryFilter(request.GET, queryset=Inventory.objects.all())
    form=inventory_filter.form
    inventory = inventory_filter.qs
    battery=Inventory.objects.filter(stock_type='BA')
    panels=Inventory.objects.filter(stock_type='PN')
    inverters=Inventory.objects.filter(stock_type='IN')
    
    battery_count = battery.count()
    panel_count = panels.count()
    inverter_count = inverters.count()
    
    context = {'inventory': inventory, 'form': form, 'battery_count': battery_count, 'panel_count': panel_count, 'inverter_count': inverter_count}
    return render(request, 'inventory_list.html', context)
   

def update_inventory(request, pk):
    inventory=Inventory.objects.get(pk=pk)
    form = InventoryCreationForm(instance=inventory)
    if request.method == 'POST':
        form = InventoryCreationForm(request.POST, instance = inventory)
    context= {'form': form}
    if form.is_valid():
            form.save()
            return redirect('inventory:inventory_list')  # Redirect to the inventory list page
    else:
        form = InventoryCreationForm()
    
    

    return render(request, 'create_inventory.html', context)
    

def delete_inventory(request, pk):
    inventory=Inventory.objects.get(pk=pk)
    if request.method == 'POST':
        inventory.delete()
        return redirect('inventory:inventory_list') 
    
    context = {'item': inventory}
    return render(request, 'delete_inventory.html', context)