# coding: utf-8
from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from .utils import ChoiceArrayField
from . import constants


class Channel(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", null=True, blank=True)
    slug = models.CharField(
        max_length=255, verbose_name="URL")
    bid_types = ChoiceArrayField(
        models.CharField(
            choices=constants.BID_TYPE_CHOICES,
            max_length=255,
            null=True,
            blank=True,
        ), help_text="Allowed comma separated values: cpc,cpm,cpa,cpv,cpi"
    )

    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('channel', kwargs=dict(pk=self.pk))

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", null=True, blank=True)
    channel = models.ForeignKey(
        "Channel", verbose_name=u"Канал", null=True, blank=True)
    bid = models.FloatField(u"Bid", null=True, blank=True)
    bid_type = models.CharField(
        choices=constants.BID_TYPE_CHOICES,
        max_length=255, verbose_name="Тип ставки", null=True, blank=True
    )

    objects = models.Manager()

    def clean(self, *args, **kwargs):
        if self.bid_type not in self.channel.bid_types:
            raise ValidationError(
                "Bid_type of Campaign should also be supported by Channel")

    def get_absolute_url(self):
        return reverse('campaign', kwargs=dict(pk=self.pk))

    def __str__(self):
        return self.name
