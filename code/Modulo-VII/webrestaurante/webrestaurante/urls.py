"""webrestaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from . import settings
from core import views
from core.urls import core_urlpatterns
from blog.urls import post_urlpatterns
from pages.urls import pages_urlpatterns
from services.urls import services_urlspatterns
from contact.urls import contact_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(core_urlpatterns)),    
    path('blog/', include(post_urlpatterns)),
    path('pages/', include(pages_urlpatterns)),
    path('services/', include(services_urlspatterns)),
    path('contact/', include(contact_urlpatterns)),
    #Ckeditor path
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT)