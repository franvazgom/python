# from django.test import TestCase
from rest_framework.test import APITestCase
import json
from projects.models import Project


class BasicTest(APITestCase):
    def setUp(self):
        self.url = '/apiTest/'
    
    def test_get(self):
        response = self.client.get(self.url, format='json')
        self.assertEquals(response.status_code, 200)

class ProjectServiceTest(APITestCase):
    def setUp(self):
        self.url = '/apiServices/'
        for i in range(10):
            Project.objects.create(
                title='Proyecto ' + str(i),
                description='description ' + str(i),
                quantity=i*3) 
    
    def test_with_out_parameters(self):
        data = {
            'parameters':{}
        }

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, 200)
        data_res = json.loads(response.data['Resultado'])
        self.assertEquals(len(data_res), 10)
        self.assertEquals(data_res[0]['title'], "Proyecto 0")

    def test_with_title_parameter(self):
        data = {
            'parameters':{'title':'Proyecto 1'}
        }

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, 200)
        data_res = json.loads(response.data['Resultado'])
        self.assertEquals(len(data_res), 1)
        self.assertEquals(data_res[0]['title'], "Proyecto 1")
    
    def test_with_description_parameter(self):
        data = {
            'parameters':{'description':'5'}
        }

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, 200)
        data_res = json.loads(response.data['Resultado'])
        self.assertEquals(len(data_res), 1)
        self.assertEquals(data_res[0]['title'], "Proyecto 5")

    def test_with_two_parameters(self):
        data = {
            'parameters':{'description':'desc', 'quantity':12}
        }

        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, 200)
        data_res = json.loads(response.data['Resultado'])
        self.assertEquals(len(data_res), 5)
        self.assertEquals(data_res[-1]['title'], "Proyecto 9")





