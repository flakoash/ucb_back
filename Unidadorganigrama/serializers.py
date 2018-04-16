from rest_framework import serializers
from .models import Unidadorganigrama
class UnidadorganigramaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidadorganigrama
        fields = '__all__'