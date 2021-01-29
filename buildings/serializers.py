from rest_framework import serializers
from .models import Home, ImageFiles


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('title', 'slug', 'photo', 'price')


class HomeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        lookup_fields = 'slug'


class ImageFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageFiles
        fields = '__all__'
        lookup_fields = 'home'
