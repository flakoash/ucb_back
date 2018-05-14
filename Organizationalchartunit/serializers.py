from rest_framework import serializers
from .models import Organizationalchartunit
from drf_dynamic_fields import DynamicFieldsMixin
class OrganizationalchartunitSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Organizationalchartunit
        fields = '__all__'