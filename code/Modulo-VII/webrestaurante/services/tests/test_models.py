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

    def test_label_name(self):
        service = self.services[0]
        field_label = service._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Título')
    
    def test_max_length(self):
        service = self.services[0]
        max_length = service._meta.get_field('title').max_length
        self.assertEquals(max_length, 200)