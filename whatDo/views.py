from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from .models import Activity
from .serializers import ActivitySerializer


class ActivityViewSet(GenericViewSet,
                        CreateModelMixin,
                        RetrieveModelMixin,
                        UpdateModelMixin,
                        ListModelMixin):
    """
    Provides a get method handler.
    """
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
