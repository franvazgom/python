from django.test import TestCase
from services.models import Service
from django.urls import reverse
from django.contrib.auth.models import User, Permission

class ServiceUserPermissionTest(TestCase):
    USER = 'pepito'
    PASSWORD = 'password'

    @classmethod
    def setUpTestData(cls):
        PERMISSION_SERVICE = 'can_edit_service'
        n = 10
        for id in range(n):
            Service.objects.create(
                title = 'Servicio ' + str(id),
                sub_title = 'Subtitulo del servicio ' + str(id),
                content = 'Contenido del servicio ' + str(id),
                image = 'Imagen del servicio ' + str(id)
            )
        user = User.objects.create(username=cls.USER, password=cls.PASSWORD, email='test@gmail.com')
        permissions = Permission.objects.filter(content_type__app_label='services',
                                                content_type__model = 'service',
                                                codename=PERMISSION_SERVICE)
        print(permissions)
        user.user_permissions.set(permissions)
        user.save()
    
    def test_view_permission_service(self):
        # resp = self.client.post('/accounts/login/', {'username':self.USER, 'password':self.PASSWORD})
        # print(resp.status_code)
        auth = self.client.login(username=self.USER, password=self.PASSWORD)
        self.assertTrue(auth)
        resp = self.client.get('/services/')
        self.assertEquals(resp.status_code, 200)
