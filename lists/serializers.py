from django.contrib.auth.models import User
from lists.models import List, Item, Profile
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    
    lists = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='list-detail'
    )

    class Meta:
        model = Profile
        fields = ('url', 'user', 'lists')


class ListSerializer(serializers.HyperlinkedModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='item-detail'
    )

    owner = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Profile.objects.all(),
        view_name='profile-detail'
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