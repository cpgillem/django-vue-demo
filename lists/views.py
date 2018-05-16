from django.contrib.auth.models import User
from rest_framework import viewsets
from lists.serializers import UserSerializer

from django.shortcuts import render
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer