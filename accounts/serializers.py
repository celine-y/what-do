from rest_framework import serializers, permissions
from .models import User, Relationship
from whatDo.serializers import EffortSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'profile_image')

class RelationshipSerializer(serializers.ModelSerializer):
    following_set = UserSerializer(
        many=False,
        read_only=True
    )

    class Meta:
        model = Relationship
        fields = ('__all__')

class UserDetailSerializer(serializers.ModelSerializer):
    effort_set = EffortSerializer(
        many=True,
        read_only=True
    )
    following = RelationshipSerializer(
        many=True,
        read_only=True
    )

    # @action(methods=['get'], detail=True, permission_classes=[
    #     permissions.IsAuthenticated
    # ])
    # def follow(self, request, pk=None):
    #     obj = get_object_or_404(User, pk=pk)
    #     user = self.request.user
    #     ct = ContentType.objects.get_for_model(obj)

    class Meta:
        model = User
        fields = ('email',
            'profile_image',
            'effort_set',
            'following')
