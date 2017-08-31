# coding: utf-8
from rest_framework import serializers

from apps.main.models import Campaign, Channel


class ChannelSerializer(serializers.ModelSerializer):
    bid_types = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Channel
        fields = ('name', 'slug', 'bid_types')


class CampaignSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()

    class Meta:
        model = Campaign
        fields = ('name', 'channel', 'bid', 'bid_type')
