from django.shortcuts import render, HttpResponseRedirect
from .models import Service
from .forms import ServiceForm
from django.contrib.admin.views.decorators import staff_member_required

def service_list(request):
    service_list = Service.objects.all()
    return render(request, 'services/service_list.html', {'service_list':service_list})

@staff_member_required()
def update(request, service_id):
    service = Service.objects.get(id=service_id)
    if request.method  == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/services')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/service_update_form.html', {'form':form})

@staff_member_required()
def create(request):
    if request.method  == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/services')
    else: # Método Get
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form':form})
