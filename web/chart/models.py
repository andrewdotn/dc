# coding: UTF-8

import hashlib
import json

from django.db import models
from django.template.defaultfilters import slugify
import django.contrib.auth.models

from common.templatetags.common_tags import user_display_name
from chart import utils

class Chart(models.Model):
    # TODO Versions 0 and 1 are now the same, run a migration so version == 1 for all data?
    VERSION = 1

    # todo

    version = models.PositiveIntegerField(default=VERSION)
    title = models.CharField(max_length=255, help_text='Chart title',
            blank=True)
    html_below_title = models.TextField(blank=True)
    sparkblocks = models.CharField(max_length=30, blank=True)
    source_title = models.CharField(max_length=255, blank=True)
    source_detail = models.TextField(blank=True)
    chart_creator_detail = models.TextField(blank=True)
    creator = models.ForeignKey(django.contrib.auth.models.User)
    # TODO: remove disqus_identifier after migrating any threads to
    # id-based identifiers
    disqus_identifier = models.TextField(max_length=20, blank=True)
    chart_data = models.TextField(default="[]")
    chart_settings = models.TextField(default="{}")
    csv_url = models.CharField(max_length=255, blank=True, default="")
    description = models.TextField(default="",
        help_text='Text-only description that goes below title when sharing '
            'on sites like Facebook', blank=True)
    y_axis_description = models.CharField(max_length=255, blank=True)
    chart_width = models.PositiveIntegerField(null=True)

    def import_chart_data(self, data):
        chart_data = utils.parse_chart_data(data)
        self.chart_data = json.dumps(chart_data)

    def creator_name(self):
        return user_display_name(self.creator)

    def creator_avatar(self):
        hash = hashlib.md5(self.creator.email.strip()).digest().encode('hex')
        return 'https://secure.gravatar.com/avatar/%s?d=identicon' % hash

    def computed_width(self, specified_width):
        final_width = 630
        if self.chart_width:
            final_width = self.chart_width
        if specified_width:
            final_width = specified_width
        return final_width

    def enclosing_width(self, specified_width):
        return int(self.computed_width(specified_width)) + 20

    def source_width(self, specified_width):
        return max(100, int(self.computed_width(specified_width)) - 155)

    def slug_title(self):
      return slugify(self.title)[:80]

    def get_absolute_url(self):
        return '/chart/%d/%s' % (self.id, self.slug_title())

    def get_disqus_identifier(self):
        if self.disqus_identifier:
            return self.disqus_identifier
        return 'chart%d' % self.id

    def __unicode__(self):
        return '(%d) %s' % (self.id, self.title)
