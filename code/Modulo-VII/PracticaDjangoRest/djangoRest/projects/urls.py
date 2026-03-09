from rest_framework import routers
from .api import ProjectViewSet
from .api_g import DataTest, ProjectServices
from django.urls import path, include

router = routers.DefaultRouter()
router.register('api/projects', ProjectViewSet, 'projects')
# urlpatterns = router.urls
urlpatterns = [
    path('api/', include(router.urls)),
    path('apiTest/', DataTest.as_view()),
    path('apiServices/', ProjectServices.as_view()),
]

