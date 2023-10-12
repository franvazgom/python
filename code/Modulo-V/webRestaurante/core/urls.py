from django.urls import path
from core import views
from django.contrib.auth import views as auth_views

core_urlpatterns = ([
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
], 'core')