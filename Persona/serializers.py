from rest_framework import serializers
from .models import Persona
from django.contrib.auth.models import User
from drf_dynamic_fields import DynamicFieldsMixin
import string
import random


class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class PersonaSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Persona
        fields = '__all__'

    def create(self, validated_data):
        user_data = self.context['user']
        if User.objects.filter(username=user_data['username']).exists():
            user = User.objects.get(username=user_data['username'])
        else:
            user = User.objects.create_user(username=user_data['username'],email=user_data['username'], password=user_data['password'])
        persona = Persona.objects.create(user = user, **validated_data)
        return persona

    def update(self, instance, validated_data):

        #instance.nombre = validated_data.get('nombre', instance.name)
        persona = Persona.objects.create(**validated_data)
        instance = persona
        instance.save()
        user_data = self.context['user']
        user = instance.user
        user.username = user_data['username']
        user.email = user_data['username']
        user.set_password(user_data['password'])
        user.save()
        return instance
