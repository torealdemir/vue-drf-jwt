from .models import MainContent
from .serializers import MainContentSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, status


class ContentListViewSet(ModelViewSet):
    queryset = MainContent.objects.all()
    serializer_class = MainContentSerializer


class ProjectCreateApiView(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = MainContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)