from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate

from apps.main.models import Channel, Campaign


class ChannelTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test_user@gmail.com',
            password='testuser'
        )
        self.client.login(
            username='testuser',
            password='testuser'
        )

    def test_create_channel_with_right_bid_types(self):
        """
        Ensure we can create a new Channel object.
        """
        url = reverse('channel-list')
        data = {
            'name': 'Test Right Channel',
            'slug': 'test-right-channel',
            'bid_types': {'cpa', 'cpi'}
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Channel.objects.count(), 1)

    def test_create_channel_with_wrong_bid_types(self):
        """
        Ensure we can't create a new Channel object with wrong bid_types.
        """
        url = reverse('channel-list')
        data = {
            'name': 'Test Wrong Channel',
            'slug': 'test-wrong-channel',
            'bid_types': {'cpa', 'blah'}
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Channel.objects.count(), 0)


class CampaignTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test_user@gmail.com',
            password='testuser'
        )
        self.client.login(
            username='testuser',
            password='testuser'
        )

        # Create a Channel for test
        Channel.objects.create(
            name='Test Channel',
            slug='test-slug',
            bid_types=['cpa', 'cpi']
        )

    def test_create_campaign_with_right_bid_type(self):
        """
        Ensure we can create a new Campaign object.
        """
        url = reverse('campaign-list')
        data = {
            'name': 'Test Campaign',
            'bid': 34.0,
            'bid_type': 'cpa',
            'channel_id': Channel.objects.get(slug='test-slug').id
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Campaign.objects.count(), 1)

    def test_create_campaign_with_wrong_bid_type(self):
        """
        Ensure we can't create a new Campaign object with a bid_type
        that is not supported by Channel.
        """
        url = reverse('campaign-list')
        data = {
            'name': 'Test Campaign',
            'bid': 34.0,
            'bid_type': 'cpv',
            'channel_id': Channel.objects.get(slug='test-slug').id
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Campaign.objects.count(), 0)
