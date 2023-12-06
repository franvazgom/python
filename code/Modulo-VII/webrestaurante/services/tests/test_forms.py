from django.test import TestCase
from services.forms import OrderForm


class TestOrderForm(TestCase):
    def test_labels(self):
        of = OrderForm()
        self.assertTrue(of.fields['name'].label == 'Nombre')
    
    def test_data_incomplete(self):
        form_data = {'email':'ddddd',
                     'name':'aaaaaaaaa',
                     'address':'lllllllllll'}
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