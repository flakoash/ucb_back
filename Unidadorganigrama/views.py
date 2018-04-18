from rest_framework import views, serializers, status
from rest_framework.response import Response
from .serializers import UnidadorganigramaSerializer
from .models import Unidadorganigrama
from django.http import Http404


class UnidadorganigramaView(views.APIView):
    def get(self, request, format=None):
        queryset = Unidadorganigrama.objects.all()
        serializer = UnidadorganigramaSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print request.data
        serializer = UnidadorganigramaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UnidadorganigramaDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Unidadorganigrama.objects.get(pk=pk)
        except Unidadorganigrama.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = UnidadorganigramaSerializer(queryset, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = UnidadorganigramaSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)