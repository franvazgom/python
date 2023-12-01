from django.test import TestCase
from services.models import Service
from django.urls import reverse

class ServiceViewTest(TestCase):
    @classmethod
    def setUpTestData(self):
        n = 9
        for id in range(n):
            Service.objects.create(
                title = 'Servicio ' + str(id),
                sub_title = 'Subtitulo del servicio ' + str(id),
                content = 'Contenido del servicio ' + str(id),
                image = 'Imagen del servicio ' + str(id)
            )
    def test_view_url_desired(self):
        resp = self.client.get('/services/')
        self.assertEquals(resp.status_code, 200)

    def test_view_service_list_template(self):
        resp = self.client.get('/services/')
        self.assertTemplateUsed(resp, 'services/service_list.html')
        self.assertTrue("Servicio 0" in str(resp.content))
    
    def test_paginated_by_two(self):
        resp = self.client.get(reverse('services:service_list'))
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['object_list']) == 2)
        self.assertTrue(len(resp.context['service_list']) == 2)

    def test_pagination_remain(self):
        resp = self.client.get(reverse('services:service_list') + '?page=5') 
        self.assertEquals(resp.status_code, 200)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue(len(resp.context['object_list']) == 1)
        self.assertTrue(len(resp.context['service_list']) == 1)
        self.assertTrue("Servicio 8" in str(resp.content))
 