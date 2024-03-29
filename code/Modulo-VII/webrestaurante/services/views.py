from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from .models import Service
from .forms import ServiceForm
from django.contrib.admin.views.decorators import staff_member_required
import json
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, ListView 
from .forms import OrderForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required

class OrderSuccessView(TemplateView):
    template_name = 'services/order_success.html'

class CreateOrder(CreateView):
    form_class = OrderForm
    template_name = 'services/order_client.html'
    success_url = reverse_lazy('services:order_success')

    def form_valid(self, form):
        order = self.request.session['order']
        for pro in order: 
            id = pro['id']
            qty = pro['quantity']
            s = Service.objects.get(pk=id)
            s.quantity = s.quantity - qty
            s.save()
        order = form.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateOrder, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


def detail_order(request):
    if request.method == 'POST':
        data = request.POST['order_data']
        #Convesión a json
        order_data = json.loads(data)
        total = 0
        order = list()
        for product in order_data.keys():
            qty = order_data[product]
            service = Service.objects.get(pk=int(product))
            dict_product = {}
            dict_product['id'] = service.id
            dict_product['title'] = service.title
            dict_product['sub_title'] = service.sub_title
            dict_product['quantity'] = qty
            dict_product['cost'] = service.cost
            dict_product['sub_total']  = service.cost * qty
            total += dict_product['sub_total'] 
            order.append(dict_product)
        # Se colocan en sesión estos datos
        request.session['total'] = total
        request.session['order'] = order
        return render(request, 'services/detail_order.html', {'order':order, 'total':total})    

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

@method_decorator(permission_required('services.can_edit_service', login_url='/accounts/login/'), name='dispatch')
class ServiceListView(ListView):
    model = Service
    paginate_by = 2