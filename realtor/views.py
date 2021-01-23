from rest_framework import permissions
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveDestroyAPIView, \
    RetrieveUpdateAPIView
from .models import Agent
from .serializers import *


class AgentListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    pagination_class = None


class AgentDetailView(RetrieveAPIView):
    # permission_classes = (permissions.AllowAny)
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    # pagination_class = None


class TopSellerListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Agent.objects.filter(top_seller=True)
    serializer_class = AgentSerializer
    pagination_class = None

