from rest_framework import views, serializers, status
from rest_framework.response import Response
from .serializers import OrganizationalchartunitSerializer
from .models import Organizationalchartunit
from django.http import Http404


class OrganizationalchartunitView(views.APIView):
    def get(self, request, format=None):
        queryset = Organizationalchartunit.objects.all()
        serializer = OrganizationalchartunitSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrganizationalchartunitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationalchartunitDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Organizationalchartunit.objects.get(pk=pk)
        except Organizationalchartunit.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = OrganizationalchartunitSerializer(queryset, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = OrganizationalchartunitSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)