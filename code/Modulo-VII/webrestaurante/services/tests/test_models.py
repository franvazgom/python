from django.test import TestCase
from services.models import Service

class TestServiceModel(TestCase):
    @classmethod
    def setUpTestData(self): 
        s = Service(title = "Prueba 1",   
            sub_title = "Subtitulo 1",
            content = 'Contenido de pruebas', 
            image = 'pruebas/prueba.jpg') 
        s.save()
        self.services = Service.objects.all()
    def test_save(self):
        self.assertEquals(len(self.services), 1)
        self.assertIs(len(self.services)>0, True )
        self.assertEquals(self.services[0].sub_title, 'Subtitulo 1')
    
    def test_service_cost(self): 
        self.assertEquals(self.services[0].cost, 500)