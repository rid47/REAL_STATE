from django.urls import path
from .views import HomeDetailAPIView, HomeListAPIView, ImageView, SearchDataAPIView

urlpatterns = [
    path('', HomeListAPIView.as_view(), name='home'),
    path('<slug>/', HomeDetailAPIView.as_view(), name='home-detail'),
    path('images/<pk>/', ImageView.as_view(), name='images'),
    path('data/search/', SearchDataAPIView.as_view(), name='search_data'),
    ]
