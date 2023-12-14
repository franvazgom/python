import json
from .models import Project

class Data:
    def get_test_service(self):
        aux = {'nombre': 'Juan Pérez'}
        return json.dumps(aux)
    
    def get_suma(self, num1, num2):
        suma = num1 + num2
        res = {'suma':suma}
        return json.dumps(res)

    # parameter es de tipo Json 
    def get_projects(self, parameters = None):
        projects = Project.objects.all()
        if parameters: 
            if 'title' in parameters: 
                # projects = projects.filter(title = parameters['title'])
                projects = projects.filter(title = parameters['title'])
            if 'description' in parameters:
                projects = projects.filter(description__contains = parameters['description'])
            if 'quantity' in parameters: 
                projects = projects.filter(quantity__gt = parameters['quantity'])
        return projects
