from rest_framework import serializers
from .models import XOXOXO
from drf_dynamic_fields import DynamicFieldsMixin
class XOXOXOSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = XOXOXO
        fields = '__all__'