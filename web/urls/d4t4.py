# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    # Some day this will be a general-purpose URL shortener

    (ur'^$', redirect_to, {
        'url': 'https://datacollective.org/sparkblocks.html',
        'permanent': False}),
)
