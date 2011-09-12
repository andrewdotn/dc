# coding: UTF-8

from django.db import models

class Chart(models.Model):
    title = models.CharField(max_length=255)
    sparkblocks = models.CharField(max_length=30, unique=True)
    tweet = models.CharField(max_length=140)
    source_url = models.URLField()
    source_title = models.CharField(max_length=255)
    source_detail = models.TextField()
    chart_creator = models.CharField(max_length=100)
    chart_creator_avatar = models.URLField()
    chart_creator_detail = models.TextField()
    disqus_identifier = models.TextField(max_length=20)
    chart_data = models.TextField()
    chart_settings = models.TextField()
    csv_url = models.URLField()
    xls_url = models.URLField()
    short_name = models.CharField(max_length=255)
    description = models.TextField(default="")

    def __unicode__(self):
        return self.title
