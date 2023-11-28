from django.test import TestCase

class TestGenerica(TestCase):
    def test_suma(self):
        a = 4
        b = 9
        suma = a + b
        self.assertEquals(suma, 13)
    
    def test_resta(self):
        a = 4
        b = 9
        resta = a - b
        self.assertEquals(resta, -5)