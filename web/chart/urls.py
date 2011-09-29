# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url

from chart.models import Chart

urlpatterns = patterns('chart.views',
    (r'^convert/(?P<chart_id>\d+)/$', 'convert'),
    (r'^embed/(?P<chart_id>\d+)/$', 'embed'),
    (r'^embedjs/(?P<chart_id>\d+)/$', 'embed_js'),
    (r'^image/(?P<chart_id>\d+)/$', 'image'),
    (r'^image/(?P<short_name>.+)/$', 'image'),
    (r'^edit/(?P<chart_id>\d+)/$', 'edit'),
    (r'^update/(?P<chart_id>\d+)/$', 'update'),
    (r'^new/$', 'new'),
    (r'^(?P<chart_id>\d+)/$', 'view'),
    (r'^(?P<short_name>.+)/$', 'view'),
    (r'^$', 'index'),
)
