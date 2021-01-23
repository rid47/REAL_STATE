from django.urls import path
from .views import *

urlpatterns = [
    path('', ContactAPIView.as_view(), name='contact'),
    ]
