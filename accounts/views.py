from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import User, Relationship
from .serializers import (UserSerializer,
    UserDetailSerializer,
    RelationshipSerializer)


class UserViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        self.object = get_object_or_404(User, pk=pk)
        serializer = UserDetailSerializer(self.object)
        return Response(serializer.data)

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

    def get(self, request, pk=None):
        self.object = get_object_or_404(User, pk=pk)
        users = self.object.followers.all()
        serializer = UserSerializer(users,
            many=True, context={'request': request})
        return Response(serializer.data)
