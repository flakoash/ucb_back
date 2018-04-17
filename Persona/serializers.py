from rest_framework import serializers
from .models import Persona
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')


class PersonaSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=False)

    class Meta:
        model = Persona
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(username=user_data['email'],email=user_data['email'], password=user_data['password'])
        persona = Persona.objects.create(user=user, **validated_data)

        return persona
