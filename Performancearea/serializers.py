from rest_framework import serializers
from .models import Performancearea
from drf_dynamic_fields import DynamicFieldsMixin
class PerformanceareaSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Performancearea
        fields = '__all__'