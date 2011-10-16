# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url

from chart.models import Chart

urlpatterns = patterns('chart.views',
    (r'^new/$', 'new'),
    # [1-9]\d* to avoid ambiguity with leading zeroes
    (r'^(?P<chart_id>[1-9]\d*)/(?P<title>[^/]+)?/?$', 'view'),
    (r'^convert/(?P<chart_id>[1-9]\d*)/$', 'convert'),
    (r'^embed/(?P<chart_id>[1-9]\d*)/?$', 'embed'),
    (r'^embedjs/(?P<chart_id>[1-9]\d*)/?$', 'embed_js'),
    (r'^image/(?P<chart_id>[1-9]\d*)/$', 'image'),
    (r'^edit/(?P<chart_id>[1-9]\d*)/$', 'edit'),
    (r'^update/(?P<chart_id>[1-9]\d*)/$', 'update'),
    (r'^convertdata/$', 'convert_data'),

    (r'^$', 'index'),
)
