from django.urls import path
from core import views

core_urlpatterns = ([
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'), 
], 'core')