from lists.models import List, Item
from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, object):
        if isinstance(object, List):
            return object.owner == request.user.profile
        elif isinstance(object, Item):
            return object.parent_list.owner == request.user.profile