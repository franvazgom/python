from django.shortcuts               import render
from django.http                    import HttpResponseRedirect
from .forms                         import ContactForm, ContactForm2
from django.urls                    import reverse_lazy
from django.http                    import JsonResponse
from django.views.decorators.http   import require_http_methods, require_POST
from django.middleware.csrf         import get_token
from pages.models                   import Page
from django.core.serializers import serialize
import pdb

@require_POST
def get_cities(request):
    token = get_token(request)
    print(token)
    selected_country = request.POST.get('country', '')
    if selected_country == 'México':
        cities = ['Ciudad de México', 'Puebla', 'Veracruz', 'Guadalajara', 'Monterrey']
    elif selected_country == 'USA':
        cities = ['Nueva York','Los Ángeles','Chicago']
    elif selected_country == 'Canada':
        cities = ['Vancouver','Mentreal','Quebec']
    else:
        cities = []
    return JsonResponse({'cities':cities})

@require_http_methods(['GET'])
def get_countries(request):

    # countries = ['México', 'USA', 'Canada']
    countries = serialize('json', Page.objects.all())
    return JsonResponse({'countries':countries})

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

