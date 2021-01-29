from django.urls import path
from .views import HomeDetailAPIView, HomeListAPIView, ImageView

urlpatterns = [
    path('', HomeListAPIView.as_view(), name='home'),
    path('<slug>/', HomeDetailAPIView.as_view(), name='home-detail'),
    path('images/<pk>/', ImageView.as_view(), name='images'),
    ]
