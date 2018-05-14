from rest_framework import views, serializers, status
from rest_framework.response import Response
from .serializers import CatalogueSerializer
from .models import Catalogue
from django.http import Http404


class CatalogueView(views.APIView):
    def get(self, request, format=None):
        queryset = Catalogue.objects.all()
        serializer = CatalogueSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CatalogueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatalogueDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Catalogue.objects.get(pk=pk)
        except Catalogue.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = CatalogueSerializer(queryset, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = CatalogueSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)