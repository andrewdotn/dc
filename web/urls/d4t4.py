# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd4t4.views.home', name='home'),
    # url(r'^d4t4/', include('d4t4.foo.urls')),

    (r'^index.html', redirect_to, {'url': '/', 'permanent': False}),

    # serve up our about page as our home page for now
    # DJ stuffed the about page into the chart app because it was expedient.
    (r'^$', 'chart.views.about'),

    (r'^chart/', include('chart.urls')),

    (ur'^(?P<sparkblocks>[▁▂▃▅▆▇]+)$', 'chart.views.sparklink'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^staff/admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^staff/admin/', include(admin.site.urls)),

    (r'^staff/sentry/', include('sentry.web.urls')),
)
