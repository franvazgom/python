from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput
from services.models import Service, Order

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        # total = self.request.session.get('total')
        total = 200
        initial = kwargs.get('initial', {})
        initial['total'] = total

        super().__init__(*args, **kwargs)
    class Meta:
        model = Order
        fields = ['email','name','address','neighborhood', 'total']

        widgets= {
            'email':EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'name':TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'address':TextInput(attrs={'class':'form-control', 'placeholder':'Dirección'}),
            'neighborhood':TextInput(attrs={'class':'form-control', 'placeholder':'Colonia'}),
            'total':TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        }
        

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'sub_title', 'content', 'image']
        widgets = {
            'title':TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'sub_title':TextInput(attrs={'class':'form-control', 'placeholder':'Sub título'}),            
        }
    #Función de validación del formulario
    def clean(self):
        super(ServiceForm, self).clean()
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            self._errors['title'] = self.error_class(['Minimo 5 caracteres'])
        return self.cleaned_data

