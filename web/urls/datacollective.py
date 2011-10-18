# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.views.generic.simple import redirect_to

from common.urls import handler404

staff_redirect = user_passes_test(lambda u: u.is_staff)(redirect_to)
staff_render = user_passes_test(lambda u: u.is_staff)(render)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', render, {'template_name': 'about.html'}, 'about'),
    (r'^index.html', redirect_to, {'url': '/', 'permanent': False}),
    (r'^sparkblocks/', render, {'template_name': 'sparkblocks.html'}),
    (r'^sparkblocks.html', redirect_to, {'url': '/sparkblocks/'}),

    (r'^chart/', include('chart.urls')),
    # https://docs.djangoproject.com/en/dev/topics/auth/#django.contrib.auth.models.User
    (r'^users/(?P<username>[a-zA-Z0-9_@+.-]+)/$', 'chart.views.charts_by_user'),

    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page' : '/'}),
    (r'^accounts/login/', redirect_to, {'url': '/login/'}),

    (r'^staff/admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^staff/admin/', include(admin.site.urls)),
    (r'^staff/sentry/', include('sentry.web.urls')),
    # debugging items:
    (r'^staff/base.html', staff_render, {'template_name': 'base.html'}),
    (r'^staff/500/', staff_render, {'template_name': 'NOTEXIST'}),
    (r'^staff/redirectloop/', staff_redirect, {'url': '/staff/redirectloop/',
            'permanent': False}),
)
