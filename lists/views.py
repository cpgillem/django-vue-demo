from django.contrib.auth.models import User
from lists.models import List, Item
from rest_framework import viewsets
from lists.serializers import UserSerializer, ListSerializer, ItemSerializer

from django.shortcuts import render
from django.http import HttpResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Lists.
    """
    # TODO: Only show lists for user
    # TODO: Include items for each list
    queryset = List.objects.all()
    serializer_class = ListSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Items.
    """
    # TODO: Only show items for user/list
    queryset = Item.objects.all()
    serializer_class = ItemSerializer