from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .serializers import HomeSerializer, HomeDetailSerializer, ImageFilesSerializer
from .models import Home, ImageFiles
from django.db.models import Q


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


class SearchDataAPIView(APIView):
    # permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        # data = self.request.data
        queryset = Home.objects.filter(is_published=True)
        try:
            str = request.data['str']
            q = (Q(description__icontains=str)) | (Q(title__icontains=str))
            queryset = queryset.filter(q)
        except:
            pass
        try:
            price_from = request.data['price_from']
            queryset = queryset.filter(price__gte=price_from)
        except:
            pass
        try:
            price_to = request.data['price_to']
            queryset = queryset.filter(price__lte=price_to)
        except:
            pass

        serializer = HomeSerializer(queryset, many=True)
        return Response(serializer.data)

