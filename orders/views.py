from django.shortcuts import get_object_or_404, render, redirect
from orders.forms import OrderCreationForm
from .models import Order
from core.filters import OrderFilter
from django.contrib import messages
# Create your views here.

def create_order(request):
    if request.method == 'POST':
        order_form = OrderCreationForm(request.POST)
        if order_form.is_valid():

            order_form.save()
            return redirect('orders:order_list')  # Redirect to the homepage after successful form submission
        else:
            messages.success(request,("There was an error, serial number already exists"))
            return redirect('orders:create_order') 
    else:
        order_filter = OrderFilter(request.GET, queryset=Order.objects.all())
        search_form=order_filter.form
        orders = order_filter.qs
        order_form = OrderCreationForm()
        context = {'orders': orders, 'search_form': search_form, 'order_form': order_form}
        
        return render(request, 'create_order.html', context)
    
def update_order(request, pk):
    orders=Order.objects.get(pk=pk)
    form = OrderCreationForm(instance=orders)
    if request.method == 'POST':
        form = OrderCreationForm(request.POST, request.FILES, instance=orders)
    context= {'order_form': form}
    if form.is_valid():
            form.save()
            return redirect('orders:create_order')  # Redirect to the order list page
    else:
        form = OrderCreationForm()
    
    return render(request, 'create_order.html', context)


def delete_order(request, pk):
    order=Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list') 
    
    context = {'item': order}
    return render(request, 'delete_order.html', context)

def order_list(request):
    order_filter = OrderFilter(request.GET, queryset=Order.objects.all())
    form=order_filter.form
    orders = order_filter.qs
    return render(request, 'order_list.html', {'orders': orders, 'form': form})

def order_detail(request, pk):
    orders = get_object_or_404(Order, pk=pk)

    context = {'order':orders}

    return render(request, 'order_detail.html', context) 

   