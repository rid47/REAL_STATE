from django.urls import path
from .views import *

urlpatterns = [
    path('', AgentListView.as_view(), name='agents'),
    path('<pk>/', AgentDetailView.as_view(), name='agent_detail'),
    path('top/seller/', TopSellerListView.as_view(), name='top_seller'),
    ]
