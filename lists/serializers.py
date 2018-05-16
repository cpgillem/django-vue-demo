from django.contrib.auth.models import User
from lists.models import List, Item
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'first_name', 'last_name')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='item-detail'
    )

    owner = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=User.objects.all(),
        view_name='user-detail'
    )

    class Meta:
        model = List
        fields = ('url', 'name', 'items', 'owner')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    parent_list = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=List.objects.all(),
        view_name='list-detail'
    )
    
    class Meta:
        model = Item
        fields = ('url', 'title', 'archived', 'parent_list')