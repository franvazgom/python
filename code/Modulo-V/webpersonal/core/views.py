from django.shortcuts import render, HttpResponse

def home(request):
    # html = '<h1>Hola Mundo</h1>'
    # return HttpResponse(html)
    return render(request, 'core/home.html')

def contact(request):
    return render(request, 'core/contact.html')