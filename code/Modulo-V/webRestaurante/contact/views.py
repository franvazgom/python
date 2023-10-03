from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse_lazy

def contact(request):
    if request.method == 'POST':
        print('Entra al metodo POST')
        form = ContactForm(request.POST)
        if form.is_valid():
            name    = form.cleaned_data.get('name')
            email   = form.cleaned_data['email']
            content = form.cleaned_data['content']
            print(name, email, content)

            #Se valida que el dominio sea gmail.com
            dominio = email[email.find('@')+1:]
            if dominio != 'gmail.com':
                form.add_error('email', 'Dominio inválido.')
                return render(request, 'contact/contact.html', {'form': form})

            # return HttpResponseRedirect('/contact/thanks/')
            return HttpResponseRedirect(reverse_lazy('contact:thanks'))
        
    else: # Método Get 
        print('Entra al ELSE que es el metodo GET')
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})

def thanks(request):
    return render(request, 'contact/thanks.html')