from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Count

from whatDo.models import Activity, Effort
from whatDo.serializers import (ActivitySerializer, EffortSerializer,
    ActivityDetailSerializer)
from whatDo.permissions import IsCreator
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action


class ActivityViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Activity.objects.annotate(
        num_efforts=Count('effort')).order_by('-num_efforts')
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def retrieve(self, request, pk=None):
        self.object = get_object_or_404(Activity, pk=pk)
        serializer = ActivityDetailSerializer(self.object)
        return Response(serializer.data)

    # @action(methods=['get'], detail=True)
    # def trending(self, request):


class EffortViewSet(viewsets.ModelViewSet):

    queryset = Effort.objects.all()
    serializer_class = EffortSerializer
    permission_classes = [IsCreator]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
