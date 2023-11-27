from django.urls import path
from services import views
from services.views import CreateOrder

services_urlspatterns = ([
    path('create_order/', CreateOrder.as_view(), name='create_order'),
    path('', views.service_list, name='service_list'),
    path('create/', views.create , name='create'),
    path('update/<int:service_id>', views.update , name='update'),
    path('detail_order/', views.detail_order, name='detail_order'),
], 'services')