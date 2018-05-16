from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'lists', views.ListViewSet)
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'api/', include(router.urls)),
]