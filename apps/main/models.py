from django.db import models
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse

from .utils import ChoiceArrayField
from . import constants


class Channel(models.Model):
    name = models.CharField(
        max_length=255, verbose_name="Название", null=True, blank=True)
    slug = models.CharField(
        max_length=255, verbose_name="URL", unique=True)
    bid_types = ChoiceArrayField(
        models.CharField(
            choices=constants.BID_TYPE_CHOICES,
            max_length=255,
            null=True,
            blank=True,
        ), help_text="Allowed comma separated values: cpc,cpm,cpa,cpv,cpi"
    )

    objects = models.Manager()

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

    def __str__(self):
        return self.name
