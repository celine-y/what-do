from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

from django.conf import settings

class IsCreator(permissions.BasePermission):
    """
    Object-level permission to only allow creators of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        message = 'You must be the creator of this object to edit.'
        if request.method in permissions.SAFE_METHODS:
            return True

        if obj.created_by == request.user:
            return True
        raise PermissionDenied({'message': message})
