from django.shortcuts import render
from .models import Page

def page(request, page_id):
    page = Page.objects.get(id=page_id)
    return render(request, 'pages/page.html',{'page':page})

