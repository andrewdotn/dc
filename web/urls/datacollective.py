# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to
from django.shortcuts import render

from common.urls import handler404

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', render, {'template_name': 'about.html'}),
    (r'^index.html', redirect_to, {'url': '/', 'permanent': False}),
    (r'^sparkblocks/', render, {'template_name': 'sparkblocks.html'}),
    (r'^sparkblocks.html', redirect_to, {'url': '/sparkblocks/'}),

    (r'^chart/', include('chart.urls')),
    # https://docs.djangoproject.com/en/dev/topics/auth/#django.contrib.auth.models.User
    (r'^users/(?P<username>[a-zA-Z0-9@+.-]+)/$', 'chart.views.charts_by_user'),
    (r'^unicode/([a-z]?)', 'chart.views.unicode_problem_debug'),

    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    (r'^accounts/login/', redirect_to, {'url': '/login/'}),

    (r'^staff/500/', 'chart.views.fivehundred'),
    (r'^staff/admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^staff/admin/', include(admin.site.urls)),
    (r'^staff/sentry/', include('sentry.web.urls')),
)
