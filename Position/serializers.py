from rest_framework import serializers
from .models import Position
from drf_dynamic_fields import DynamicFieldsMixin
class PositionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'