# coding: utf-8
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Campaign, Channel


# Example of CBV methods without DRF
class ChannelList(ListView):
    model = Channel


class ChannelCreate(CreateView):
    model = Channel
    success_url = reverse_lazy('channel_list')
    fields = '__all__'


class ChannelUpdate(UpdateView):
    model = Channel
    success_url = reverse_lazy('channel_list')
    fields = '__all__'


class ChannelDelete(DeleteView):
    model = Channel
    success_url = reverse_lazy('channel_list')


# Campaign methods
class CampaignList(ListView):
    model = Campaign


class CampaignCreate(CreateView):
    model = Campaign
    success_url = reverse_lazy('campaign_list')
    fields = '__all__'


class CampaignUpdate(UpdateView):
    model = Campaign
    success_url = reverse_lazy('campaign_list')
    fields = '__all__'


class CampaignDelete(DeleteView):
    model = Campaign
    success_url = reverse_lazy('campaign_list')
