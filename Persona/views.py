from rest_framework import views, serializers, status
from rest_framework.response import Response
from .serializers import PersonaSerializer
from .models import Persona
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework.parsers import MultiPartParser, ParseError


class PersonaView(views.APIView):
    def get(self, request, format=None):
        queryset = Persona.objects.all()
        serializer = PersonaSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PersonaSerializer(data=request.data,context={'user': request.data['user']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonaDetailView(views.APIView):
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False

    def get_object_by_usrname(self, pk):
        try:
            return Persona.objects.get(user__username=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get_object(self, pk):
        try:
            return Persona.objects.get(id=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get_queryset(self,pk):
        if self.is_number(pk):
            queryset = self.get_object(pk)
        else:
            queryset = self.get_object_by_usrname(pk)
        return queryset

    def get(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = PersonaSerializer(queryset, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = PersonaSerializer(queryset, data=request.data, context={'user': request.data['user']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class imageUpload(views.APIView):
    #parser_classes = MultiPartParser

    def post(self, request, format=None):
        try:
            file = request.data['photo']
        except KeyError:
            raise ParseError('Request has no resource file attached')
        username = request.data['username']
        print username
        person = Persona.objects.get(user__username=username)
        person.photo.delete(save=True)
        person.photo = file
        person.save()
        return Response(status=status.HTTP_201_CREATED)
