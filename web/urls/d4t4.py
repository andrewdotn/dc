# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd4t4.views.home', name='home'),
    # url(r'^d4t4/', include('d4t4.foo.urls')),

    (r'^$', redirect_to, {'url': 'static/html/about.html'}),

    (r'^chart/', include('chart.urls')),

    (ur'^(?P<sparkblocks>[▁▂▃▅▆▇]+)$', 'chart.views.sparklink'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
