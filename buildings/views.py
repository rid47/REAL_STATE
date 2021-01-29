from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import HomeSerializer, HomeDetailSerializer, ImageFilesSerializer
from .models import Home, ImageFiles


class HomeListAPIView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = HomeSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'


class HomeDetailAPIView(RetrieveAPIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = HomeDetailSerializer
    queryset = Home.objects.filter(is_published=True).order_by('-list_date')
    lookup_field = 'slug'


class ImageView(APIView):
    def get(self, request, pk, format=None):
        home = Home.objects.get(pk=pk)
        images = home.images.all()
        serilizer = ImageFilesSerializer(images, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)

