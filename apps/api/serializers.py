from rest_framework import serializers

from apps.main.models import Campaign, Channel
from apps.main import constants


class ChannelSerializer(serializers.ModelSerializer):
    bid_types = serializers.ListField(child=serializers.CharField())

    def validate_bid_types(self, value):
        if not set(value).issubset(
                [i[0] for i in constants.BID_TYPE_CHOICES]):
            raise serializers.ValidationError(
                "Specified value of bid_types field is not allowed.")
        return value

    class Meta:
        model = Channel
        fields = ('name', 'slug', 'bid_types')


class CampaignSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer(read_only=True)

    channel_id = serializers.PrimaryKeyRelatedField(
        source='channel',
        queryset=Channel.objects.all(),
        required=False
    )

    def validate(self, data):
        if data['bid_type'] not in data['channel'].bid_types:
            raise serializers.ValidationError(
                "Bid_type of Campaign should also be supported by Channel")
        return data

    class Meta:
        model = Campaign
        fields = ('name', 'channel_id', 'channel', 'bid', 'bid_type')
