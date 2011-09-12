# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url

from chart.models import Chart

urlpatterns = patterns('chart.views',
    (r'^convert/(?P<chart_id>\d+)/$', 'convert'),
    (r'^embed/(?P<chart_id>\d+)/$', 'embed'),
    (r'^image/(?P<chart_id>\d+)/$', 'image'),
    (r'^image/(?P<short_name>.+)/$', 'image'),
    (r'^(?P<chart_id>\d+)/$', 'view'),
    (r'^(?P<short_name>.+)/$', 'view'),
    (r'^$', 'index'),
)
