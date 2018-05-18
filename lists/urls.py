from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path

from . import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'lists', views.ListViewSet)
router.register(r'items', views.ItemViewSet)

urlpatterns = [
    # Single-page frontend view.
    path(r'', views.index, name='index'),

    # API Views.
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'rest-auth/registration', include('rest_auth.registration.urls')),
    url(r'rest-auth/', include('rest_auth.urls')),
    path(r'api/', include(router.urls)),
]