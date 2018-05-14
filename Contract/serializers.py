from rest_framework import serializers
from .models import Contract
from drf_dynamic_fields import DynamicFieldsMixin
class ContractSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'