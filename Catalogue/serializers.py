from rest_framework import serializers
from .models import Catalogue
from drf_dynamic_fields import DynamicFieldsMixin
class CatalogueSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Catalogue
        fields = '__all__'