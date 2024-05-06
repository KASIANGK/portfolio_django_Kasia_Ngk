from django.shortcuts import render, redirect
from .models import Service
from .forms import ServiceForm
from django.forms import modelformset_factory


def service(request):
    services = Service.objects.first()
    return render(request, 'services.html', {'services': services})



def modify_services(request):
    data_saved = False
    serviceform = Service.objects.all()
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('homeback')  
    else:
        form = ServiceForm()
    
    return render(request, 'services_editable.html', {'form': form, 'data_saved': data_saved, 'serviceform':serviceform})
