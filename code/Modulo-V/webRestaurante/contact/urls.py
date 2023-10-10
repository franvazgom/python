from django.urls import path
from contact import views

contact_urlpatterns = ([
    path('', views.contact, name='contact'),
    path('thanks/', views.thanks, name='thanks'),
    path('get_countries/', views.get_countries, name='get_countries'),
    path('get_cities/', views.get_cities, name='get_cities'),
], 'contact')

