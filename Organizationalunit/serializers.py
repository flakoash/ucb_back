from rest_framework import serializers
from .models import Organizationalunit
from drf_dynamic_fields import DynamicFieldsMixin
class OrganizationalunitSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Organizationalunit
        fields = '__all__'