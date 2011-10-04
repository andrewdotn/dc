# coding: UTF-8

import hashlib
import json

from django.db import models
import django.contrib.auth.models

from chart import utils

# Haven’t figured this out properly yet
# https://docs.djangoproject.com/en/dev/topics/db/models/#model-inheritance

class Chart(models.Model):
    # TODO Versions 0 and 1 are now the same, run a migration so version == 1 for all data?
    VERSION = 1

    # todo

    version = models.PositiveIntegerField(default=VERSION)
    title = models.CharField(max_length=255, help_text='Chart title',
            blank=True)
    html_below_title = models.TextField(blank=True)
    sparkblocks = models.CharField(max_length=30, blank=True)
    tweet = models.CharField(max_length=140, blank=True)
    source_title = models.CharField(max_length=255, blank=True)
    source_detail = models.TextField(blank=True)
    chart_creator_detail = models.TextField(blank=True)
    creator = models.ForeignKey(django.contrib.auth.models.User)
    disqus_identifier = models.TextField(max_length=20, blank=True)
    chart_data = models.TextField(default="[]")
    chart_settings = models.TextField(default="{}")
    csv_url = models.CharField(max_length=255, blank=True, default="")
    short_name = models.CharField(max_length=255, blank=True)
    description = models.TextField(default="",
        help_text='Text-only description that goes below title when sharing '
            'on sites like Facebook', blank=True)
    y_axis_description = models.CharField(max_length=255, blank=True)
    chart_width = models.PositiveIntegerField(null=True)

    def import_chart_data(self, data):
        chart_data = utils.parse_chart_data(data)
        self.chart_data = json.dumps(chart_data)

    def creator_name(self):
        return '%s %s' % (self.creator.first_name, self.creator.last_name)

    def creator_avatar(self):
        hash = hashlib.md5(self.creator.email.strip()).digest().encode('hex')
        return 'https://secure.gravatar.com/avatar/%s?d=identicon' % hash

    def enclosing_width(self):
        if self.chart_width:
            return self.chart_width + 20
        else:
            return 650

    def source_width(self):
        if self.chart_width:
            return max(100, self.chart_width - 155)
        else:
            return 475

    def __unicode__(self):
        return self.title
