from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'', include(router.urls)),
]