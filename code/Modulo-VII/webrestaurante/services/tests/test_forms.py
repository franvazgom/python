from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from services.forms import OrderForm
from django.http import HttpRequest

class TestOrderForm(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        

    def test_labels(self):
        of = OrderForm()
        self.assertTrue(of.fields['name'].label == 'Nombre')
    
    def test_data_incomplete(self):
        form_data = {'email':'ddddd',
                     'name':'aaaaaaaaa',
                     'address':'lllllllllll'}
        self.client.session['total'] = 200
        self.client.session.save()
        
        of = OrderForm(form_data)
        self.assertFalse(of.is_valid())

    def test_valid_form(self):
        form_data = {'email':'ddddd@yahoo.com',
                     'name':'aaaaaaaaa',
                     'address':'lllllllllll',
                     'neighborhood':'zzzzzzzz',
                     'total':1500}
        of = OrderForm(form_data)
        self.assertTrue(of.is_valid())
    def test_email_not_valid(self): 
        form_data = {'email':'ddddd',
                     'name':'aaaaaaaaa',
                     'address':'lllllllllll',
                     'neighborhood':'zzzzzzzz',
                     'total':1500}
        of = OrderForm(form_data)
        self.assertFalse(of.is_valid())