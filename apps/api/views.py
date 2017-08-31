# coding: utf-8
from rest_framework import viewsets, generics
from apps.main.models import Campaign, Channel
from .serializers import CampaignSerializer, ChannelSerializer


# ViewSet version
class ChannelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Channel to be viewed or edited.
    """
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CampaignViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Campaign to be viewed or edited.
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer



# Generic CBV version (without wiring up to certain URLs)
class ChannelList(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CampaignList(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


class CampaignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
