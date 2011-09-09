# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    (r'', include('urls.d4t4')),

    (r'^$', redirect_to, {'url': 'index.html'}),

    (r'^(?P<filename>[a-z-]+.html)$', 'pageset.views.byfilename',
     {'pageset_name': 'datacollective'}),

    (r'^(?P<filename>[a-z-]+.html)$', 'pageset.views.byfilename',
     {'pageset_name': 'datacollective'}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
