from rest_framework import serializers
from .models import Level
from drf_dynamic_fields import DynamicFieldsMixin
class LevelSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'