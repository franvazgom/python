from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.urls import reverse_lazy
from django.core import mail
from django.http import JsonResponse
import time

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            
            pos_arroba = email.find('@')
            domino = email[pos_arroba+1:]
            subject = 'Hello La Recova'
            body = 'Body goes here' 
            from1 = 'franvazgomdev@gmail.com'
            to1 = ['franvazgom@gmail.com',]
            with mail.get_connection() as connection:
                mail.EmailMessage(                   
                    subject, body, from1, to=to1,
                    connection=connection,
                ).send()            
            

            if domino != "gmail.com":            
                form.add_error('email', 'dominio inválido')
                return render(request, 'contact/contact.html', {'form':form})
            else: 
                return HttpResponseRedirect(reverse_lazy('contact:thanks'))
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form':form})

def thanks(request):
    return render(request, 'contact/thanks.html')
