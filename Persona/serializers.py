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

        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.codUCB = validated_data.get('codUCB', instance.codUCB)
        instance.documento = validated_data.get('documento', instance.documento)
        instance.primerApellido = validated_data.get('primerApellido', instance.primerApellido)
        instance.segundoApellido = validated_data.get('segundoApellido', instance.segundoApellido)
        instance.apCasada = validated_data.get('apCasada', instance.apCasada)
        instance.fechaNacimiento = validated_data.get('fechaNacimiento', instance.fechaNacimiento)
        instance.genero = validated_data.get('genero', instance.genero)
        instance.nacionalidad = validated_data.get('nacionalidad', instance.nacionalidad)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        user_data = self.context['user']

        user = instance.user
        user.username = user_data['username']
        user.email = user_data['username']
        user.set_password(user_data['password'])
        user.save()
        return instance
