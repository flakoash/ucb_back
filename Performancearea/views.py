from rest_framework import views, serializers, status
from rest_framework.response import Response
from .serializers import PerformanceareaSerializer
from .models import Performancearea
from django.http import Http404


class PerformanceareaView(views.APIView):
    def get(self, request, format=None):
        queryset = Performancearea.objects.all()
        serializer = PerformanceareaSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PerformanceareaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PerformanceareaDetailView(views.APIView):
    def get_object(self, pk):
        try:
            return Performancearea.objects.get(pk=pk)
        except Performancearea.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = PerformanceareaSerializer(queryset, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = PerformanceareaSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)