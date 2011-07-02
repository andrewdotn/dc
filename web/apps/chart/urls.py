# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url

from chart.models import Chart

urlpatterns = patterns('',
    (r'^(?P<chart_id>\d+)/$', 'chart.views.view'),
    (r'^$', 'chart.views.index'),
)
