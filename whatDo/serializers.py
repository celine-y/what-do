from rest_framework import serializers
from .models import Activity, Effort


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_on')

class EffortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Effort
        fields = ('__all__')
        read_only_fields = ('created_by', 'created_on')
