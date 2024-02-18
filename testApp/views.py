from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer
from .forms import CustomerForm
from django.shortcuts import get_object_or_404

def home(request):
    qs = Customer.objects.all()
    return render(request, 'testApp/home.html', {'qs':qs})

def create(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Data submitted successfully")
        
    return render(request, 'testApp/create.html', {'form':form})


def update(request, pk):
    instance = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(request.POST or None, instance=instance)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse("Data updated Success")
    return render(request, 'testApp/edit.html', {'form':form})

def delete(request, pk):
    qs = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        qs.delete()
        return HttpResponse("Deleting Success")
    context = {}
    return render(request, 'testApp/delete.html', context)

