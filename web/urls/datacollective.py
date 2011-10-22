# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from django.shortcuts import render
from django.views.generic.simple import direct_to_template, redirect_to

import django.contrib.auth.views as auth_views

from common.urls import handler404, handler500

from dc.forms import DCRegistrationForm

staff_redirect = user_passes_test(lambda u: u.is_staff)(redirect_to)
staff_render = user_passes_test(lambda u: u.is_staff)(render)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', render, {'template_name': 'about.html'}, 'about'),
    (r'^speed$', render, {'template_name': 'about_speed.html'}, 'about'),
    (r'^index.html', redirect_to, {'url': '/', 'permanent': False}),
    (r'^sparkblocks/', render, {'template_name': 'sparkblocks.html'}),
    (r'^sparkblocks.html', redirect_to, {'url': '/sparkblocks/'}),

    (r'^chart/', include('chart.urls')),

    (ur'^(?P<sparkblocks>[▁▂▃▅▆▇]+)$', 'chart.views.sparklink'),

    # https://docs.djangoproject.com/en/dev/topics/auth/#django.contrib.auth.models.User
    url(r'^users/(?P<username>[\w@+.-]+)/$', 'chart.views.charts_by_user'),
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout, {'next_page' : '/'}),

    (r'^register/$', 'registration.views.register',
            {'form_class': DCRegistrationForm}),
    (r'^activate/(?P<activation_key>\w+)$',
        'registration.views.activate', {}, 'registration_activate'),

    (r'^register/complete/$', render,
        {'template_name': 'registration/confirm_account.html'},
        'registration_complete'),

    # old login URL -- remove if we’re not getting any more hits
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
