from rest_framework import serializers
from .models import Unidadorganigrama
from drf_dynamic_fields import DynamicFieldsMixin


class UnidadorganigramaSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Unidadorganigrama
        fields = '__all__'