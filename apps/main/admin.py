# coding: utf-8
from django.contrib import admin

from .models import Campaign, Channel


class CampaignInline(admin.TabularInline):
    model = Campaign


class ChannelAdmin(admin.ModelAdmin):
    inlines = [
        CampaignInline,
    ]


admin.site.register(Channel, ChannelAdmin)
admin.site.register(Campaign)
