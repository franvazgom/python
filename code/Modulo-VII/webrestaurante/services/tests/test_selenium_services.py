from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth.models import User, Permission
from services.models import Service as Servicio
import time


class TestSeleniumServices(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        PATH_WEBDRIVER = r'C:\Users\Francisco\Downloads\chromedriver-win64\chromedriver.exe'
        service = Service(PATH_WEBDRIVER)
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.set_window_size(1600, 1000)
        PERMISSION_SERVICE = 'can_edit_service'
        n = 10
        for id in range(n):
            Servicio.objects.create(
                title = 'Servicio ' + str(id),
                sub_title = 'Subtitulo del servicio ' + str(id),
                content = 'Contenido del servicio ' + str(id),
                image = 'Imagen del servicio ' + str(id)
            )
        user = User.objects.create_user(username='pepito', password='password', email='test@gmail.com')
        permissions = Permission.objects.filter(content_type__app_label='services',
                                                content_type__model = 'service',
                                                codename=PERMISSION_SERVICE)
        user.user_permissions.set(permissions)
        user.save()
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDown
    
    def test_home(self):
        browser = self.driver
        url = self.live_server_url
        browser.get(url + '/')
        time.sleep(1)
        self.assertIn('La Recova', browser.title)
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('La Recova', body.text)

    def autentica(self):
        browser = self.driver
        url = self.live_server_url
        browser.get(url + '/accounts/login/')
        user_box = browser.find_element(By.ID, 'id_username')
        password_box = browser.find_element(By.ID, 'id_password')
        btn_submit = browser.find_element(By.ID, 'btn_submit')
        user_box.send_keys('pepito')
        password_box.send_keys('password')        
        btn_submit.click() 

    def test_login(self):
        self.autentica()
        browser = self.driver
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('La Recova', body.text)
        time.sleep(1)

    def test_cart(self):
        self.autentica()
        browser = self.driver
        url = self.live_server_url
        browser.get(url + '/services/')
        # time.sleep(1)
        btn_add_cart = browser.find_element(By.LINK_TEXT, 'Agregar al carrito')
        btn_add_cart.click()
        # time.sleep(1)
        btn_badge = browser.find_element(By.ID, 'cart-badge')
        btn_badge.click()
        # time.sleep(2)
        body = browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Total = $100.00', body.text)
        # time.sleep(1)
        # Se realiza la compra
        btn_compra = browser.find_element(By.CLASS_NAME, "btn")
        btn_compra.click()
        time.sleep(2)
        caja_total = browser.find_element(By.ID, "id_total")                        
        self.assertIn('100.0', caja_total.get_attribute('value') )        
        time.sleep(2)


