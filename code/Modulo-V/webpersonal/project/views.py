from django.shortcuts import render
from . models import Project

def project(request):
    # Se obtienen todos los proyectos en la base de datos
    projects = Project.objects.all()
    return render(request, 'project/portfolio.html', {'projects':projects})
