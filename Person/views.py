from rest_framework import views, serializers, status
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person
from django.http import Http404
from rest_framework.parsers import MultiPartParser, ParseError



class PersonView(views.APIView):
    def get(self, request, format=None):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PersonSerializer(data=request.data,context={'user': request.data['user']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonDetailView(views.APIView):
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
            return Person.objects.get(user__username=pk)
        except Person.DoesNotExist:
            raise Http404

    def get_object(self, pk):
        try:
            return Person.objects.get(id=pk)
        except Person.DoesNotExist:
            raise Http404

    def get_queryset(self,pk):
        if self.is_number(pk):
            queryset = self.get_object(pk)
        else:
            queryset = self.get_object_by_usrname(pk)
        return queryset

    def get(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = PersonSerializer(queryset, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_queryset(pk)
        serializer = PersonSerializer(queryset, data=request.data, context={'user': request.data['user']})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
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
        person = Person.objects.get(user__username=username)
        person.photo.delete(save=True)
        person.photo = file
        person.save()
        return Response(status=status.HTTP_201_CREATED)