from django.shortcuts import render, redirect
from core.filters import BatteryFilter , PanelFilter, InverterFilter, BrandFilter
from inventory.forms import BatteryForm, PanelForm, InverterForm, BrandForm
from .models import Battery, Panel, Inverter, Brand
from django.contrib import messages

# Create your views here.



def add_battery(request):
    
    if request.method == 'POST':
        battery_form = BatteryForm(request.POST)
        if battery_form.is_valid():

            battery_form.save()
            return redirect('add_battery')  # Redirect to the homepage after successful form submission
        else:
            messages.success(request,("There was an error, serial number already exists"))
            return redirect('add_battery') 
    else:
        battery_filter = BatteryFilter(request.GET, queryset=Battery.objects.all())
        search_form=battery_filter.form
        batterys = battery_filter.qs
        battery_form = BatteryForm()
        context = {'batterys': batterys, 'search_form': search_form, 'battery_form': battery_form}
        
        return render(request, 'battery_list.html', context)
    
def update_battery(request, pk):
    battery=Battery.objects.get(pk=pk)
    form = BatteryForm(instance=battery)
    if request.method == 'POST':
        form = BatteryForm(request.POST, request.FILES, instance=battery)
    context= {'form': form}
    if form.is_valid():
            form.save()
            return redirect('add_battery')  # Redirect to the panel list page
    else:
        form = BatteryForm()
    
    return render(request, 'battery_update.html', context)

def delete_battery(request, pk):
    battery=Battery.objects.get(pk=pk)
    if request.method == 'POST':
        battery.delete()
        return redirect('add_battery') 
    
    context = {'item': battery}
    return render(request, 'battery_delete.html', context)

       


def add_panel(request):
    if request.method == 'POST':
        panel_form = PanelForm(request.POST)
        if panel_form.is_valid():
            panel_form.save()
            return redirect('add_panel')  # Redirect to the panel page after successful form submission
        else:
            messages.success(request,("There was an error, serial number already exists"))
            return redirect('add_panel') 
    else:
        panel_filter = PanelFilter(request.GET, queryset=Panel.objects.all())
        search_form=panel_filter.form
        panels = panel_filter.qs
        panel_form = PanelForm()
        context = {'panels': panels, 'search_form': search_form, 'panel_form': panel_form}
        
        return render(request, 'panel_list.html', context)

def update_panel(request, pk):
    panel=Panel.objects.get(pk=pk)
    form = PanelForm(instance=panel)
    if request.method == 'POST':
        form = PanelForm(request.POST, request.FILES, instance=panel)
    context= {'form': form}
    if form.is_valid():
            form.save()
            return redirect('add_panel')  # Redirect to the panel list page
    else:
        form = PanelForm()
    
    return render(request, 'panel_update.html', context)

def delete_panel(request, pk):
    panel=Panel.objects.get(pk=pk)
    if request.method == 'POST':
        panel.delete()
        return redirect('add_panel') # Redirect to the panel list page 
    
    context = {'item': panel}
    return render(request, 'panel_delete.html', context)


def add_inverter(request):
    if request.method == 'POST':
        inverter_form = InverterForm(request.POST)
        if inverter_form.is_valid():
            inverter_form.save()
            return redirect('add_inverter')  # Redirect to the inverter page after successful form submission
        else:
            messages.success(request,("There was an error, serial number already exists"))
            return redirect('add_inverter') 
    else:
        inverter_filter = InverterFilter(request.GET, queryset=Inverter.objects.all())
        search_form=inverter_filter.form
        inverters = inverter_filter.qs
        inverter_form = InverterForm()
        context = {'inverters': inverters, 'search_form': search_form, 'inverter_form': inverter_form}
        
        return render(request, 'inverter_list.html', context)

def update_inverter(request, pk):
    job=Inverter.objects.get(pk=pk)
    form = InverterForm(instance=job)
    if request.method == 'POST':
        form = InverterForm(request.POST, request.FILES, instance=job)
    context= {'form': form}
    if form.is_valid():
            form.save()
            return redirect('add_inverter')  # Redirect to the inveretr list page
    else:
        form = InverterForm()
    
    return render(request, 'inverter_update.html', context)

def delete_inverter(request, pk):
    inverter=Inverter.objects.get(pk=pk)
    if request.method == 'POST':
        inverter.delete()
        return redirect('add_inverter') # Redirect to the inverter list page 
    
    context = {'item': inverter}
    return render(request, 'inverter_delete.html', context)


def inventory_list(request):
    batteries= Battery.objects.all()
    panels= Panel.objects.all()
    inverters= Inverter.objects.all()
    in_use_batteries = Battery.objects.filter(in_use=True)
    available_batteries = Battery.objects.filter(in_use=False)
    in_use_panels = Panel.objects.filter(in_use=True)
    available_panels= Panel.objects.filter(in_use=False)
    in_use_inverters = Inverter.objects.filter(in_use=True)
    available_inverters= Inverter.objects.filter(in_use=False)

    context = {'batteries': batteries,'in_use_batteries':in_use_batteries, 'available_batteries':available_batteries, 'panels': panels, 'in_use_panels':in_use_panels,'available_panels':available_panels,'inverters': inverters, 'in_use_inverters':in_use_inverters, 'available_inverters':available_inverters}
    return render(request, 'inventory_list.html', context)


def add_brand(request):
    
    if request.method == 'POST':
        brand_form = BrandForm(request.POST)
        if brand_form.is_valid():

            brand_form.save()
            return redirect('add_brand')  # Redirect to the homepage after successful form submission
        else:
            messages.success(request,("There was an error, serial number already exists"))
            return redirect('add_brand') 
    else:
        brand_filter = BrandFilter(request.GET, queryset=Brand.objects.all())
        search_form=brand_filter.form
        brands = brand_filter.qs
        brand_form = BrandForm()
        context = {'brands': brands, 'search_form': search_form, 'brand_form': brand_form}
        
        return render(request, 'brand_list.html', context)
    
def update_brand(request, pk):
    brand=Brand.objects.get(pk=pk)
    form = BrandForm(instance=brand)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
    context= {'form': form}
    if form.is_valid():
            form.save()
            return redirect('add_brand')  # Redirect to the panel list page
    else:
        form = BrandForm()
    
    return render(request, 'brand_update.html', context)

def delete_brand(request, pk):
    brand=Brand.objects.get(pk=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('add_brand') 
    
    context = {'item': brand}
    return render(request, 'brand_delete.html', context)