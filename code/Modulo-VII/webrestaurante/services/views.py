from django.shortcuts import render, HttpResponseRedirect
from .models import Service
from .forms import ServiceForm
from django.contrib.admin.views.decorators import staff_member_required

def detail_order(request):
    return render(request, 'services/detail_order.html')

@staff_member_required()
def update(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():                        
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_update_form.html', {'form':form})

@staff_member_required()
def create(request):
    if request.method == 'POST':        
        form = ServiceForm(request.POST, request.FILES)                
        if form.is_valid():                        
            new_service = form.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'services/service_form.html', {'form':form})
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form':form})

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/service_list.html', {'services':services})
