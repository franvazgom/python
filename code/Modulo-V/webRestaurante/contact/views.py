from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm, ContactForm2
from django.urls import reverse_lazy

def contact(request):
    if request.method == 'POST':
        form = ContactForm2(request.POST)
        if form.is_valid():
            name    = form.cleaned_data.get('name')
            email   = form.cleaned_data['email']
            content = form.cleaned_data['content']
            print(name, email, content)

            # #Se valida que el dominio sea gmail.com
            # dominio = email[email.find('@')+1:]
            # if dominio != 'gmail.com':
            #     form.add_error('email', 'Dominio inválido.')
            #     return render(request, 'contact/contact.html', {'form': form})

            # return HttpResponseRedirect('/contact/thanks/')
            return HttpResponseRedirect(reverse_lazy('contact:thanks'))
        else: 
            print('Formulario inválido')
            errors = form.errors
            return render(request, 'contact/contact.html', {'form': form, 'errors':errors})
        
    else: # Método Get 
        print('Entra al ELSE que es el metodo GET')
        # form = ContactForm()
        # return render(request, 'contact/contact.html', {'form': form})
        return render(request, 'contact/contact.html')

def thanks(request):
    return render(request, 'contact/thanks.html')