from django.urls import path
from blog import views

post_urlpatterns = ([    
    path('', views.post, name='post_list'),
    path('category/<int:category_id>', views.category, name='category'),
], 'post')