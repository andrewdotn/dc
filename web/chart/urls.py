# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url

from chart.models import Chart

urlpatterns = patterns('',
    (r'^convert/(?P<chart_id>\d+)/$', 'chart.views.convert'),
    (r'^image/(?P<chart_id>\d+)/$', 'chart.views.image'),
    (r'^(?P<chart_id>\d+)/$', 'chart.views.view'),
    (r'^(?P<short_name>.+)/$', 'chart.views.view'),
    (r'^$', 'chart.views.index'),
)
