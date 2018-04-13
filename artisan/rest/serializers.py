from rest_framework import serializers
from .models import XOXOXO
class XOXOXOSerializer(serializers.ModelSerializer):
    class Meta:
        model = XOXOXO
        fields = '__all__'