from django.urls import path
from pages import views

pages_urlpatterns = ([
    path('<int:page_id>', views.page, name='page'),
], 'pages')

