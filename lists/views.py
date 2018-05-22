from django.contrib.auth.models import User
from lists.models import List, Item, Profile
from rest_framework import viewsets
from lists.serializers import ProfileSerializer, ListSerializer, ItemSerializer

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Users.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    

class ListViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Lists.
    """
    # TODO: Only show lists for user
    # TODO: Include items for each list
    serializer_class = ListSerializer

    def get_queryset(self):
        return self.request.user.profile.lists.all()


class ItemViewSet(viewsets.ModelViewSet):
    """
    API Endpoint for Items.
    """
    # TODO: Only show items for user/list
    queryset = Item.objects.all()
    serializer_class = ItemSerializer