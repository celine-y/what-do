from rest_framework import viewsets
from .models import Activity, Effort
from .serializers import ActivitySerializer, EffortSerializer
from .permissions import IsCreator
from rest_framework.permissions import IsAdminUser


class ActivityViewSet(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class EffortViewSet(viewsets.ModelViewSet):

    queryset = Effort.objects.all()
    serializer_class = EffortSerializer
    permission_classes = [IsCreator]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
