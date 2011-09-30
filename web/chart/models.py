# coding: UTF-8

import json

from django.db import models
from chart import utils

class Chart(models.Model):
    # TODO Versions 0 and 1 are now the same, run a migration so version == 1 for all data?
    VERSION = 1

    # todo

    version = models.PositiveIntegerField(default=VERSION)
    title = models.CharField(max_length=255, help_text='Chart title')
    html_below_title = models.TextField(blank=True)
    sparkblocks = models.CharField(max_length=30, blank=True)
    tweet = models.CharField(max_length=140)
    source_url = models.URLField()
    source_title = models.CharField(max_length=255)
    source_detail = models.TextField()
    chart_creator = models.CharField(max_length=100)
    chart_creator_avatar = models.URLField()
    chart_creator_detail = models.TextField()
    disqus_identifier = models.TextField(max_length=20)
    chart_data = models.TextField(default="[]")
    chart_settings = models.TextField(default="{}")
    csv_url = models.URLField(blank=True)
    xls_url = models.URLField(blank=True)
    short_name = models.CharField(max_length=255)
    description = models.TextField(default="",
        help_text='Text-only description that goes below title when sharing '
            'on sites like Facebook')
    y_axis_description = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return self.title
