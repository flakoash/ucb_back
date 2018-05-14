from rest_framework import serializers
from .models import Regional
from drf_dynamic_fields import DynamicFieldsMixin
class RegionalSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Regional
        fields = '__all__'