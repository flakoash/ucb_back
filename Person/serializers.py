from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User
from drf_dynamic_fields import DynamicFieldsMixin

class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')


class PersonSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        user_data = self.context['user']
        if User.objects.filter(username=user_data['username']).exists():
            user = User.objects.get(username=user_data['username'])
        else:
            user = User.objects.create_user(username=user_data['username'], email=user_data['username'],
                                            password=user_data['password'])
        person = Person.objects.create(user=user, **validated_data)
        return person

    def update(self, instance, validated_data):

        instance.names = validated_data.get('names', instance.nombre)
        instance.codUCB = validated_data.get('codUCB', instance.codUCB)
        instance.document = validated_data.get('document', instance.document)
        instance.typedocument = validated_data.get('typedocument', instance.typedocument)
        instance.issued = validated_data.get('issued', instance.issued)
        instance.firstsurname = validated_data.get('firstsurname', instance.firstsurname)
        instance.secondsurname = validated_data.get('secondsurname', instance.secondsurname)
        instance.mariedsurname = validated_data.get('mariedsurname', instance.mariedsurname)
        instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.nationality = validated_data.get('nationality', instance.nationality)
        instance.active = validated_data.get('active', instance.active)
        instance.phonenumber = validated_data.get('phonenumber', instance.phonenumber)
        instance.personalemail = validated_data.get('personalemail', instance.personalemail)
        instance.ucbemail = validated_data.get('ucbemail', instance.ucbemail)
        instance.officephonenumber = validated_data.get('officephonenumber', instance.officephonenumber)
        instance.homeaddress = validated_data.get('homeaddress', instance.homeaddress)
        instance.maritalstatus = validated_data.get('maritalstatus', instance.maritalstatus)

        instance.save()
        user_data = self.context['user']

        user = instance.user
        user.username = user_data['username']
        user.email = user_data['username']
        user.set_password(user_data['password'])
        user.save()
        return instance
