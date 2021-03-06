# coding: UTF-8

from django.conf.urls.defaults import patterns, include, url
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.template import Context, Template, Library
from django.views.generic.simple import redirect_to
from django.shortcuts import render
from settings.common import STATIC_ROOT

def handler404(request):
    t = Template("""\
<html>
  <head>
    <title>404 Not Found</title>
  </head>
  <body>
    <h1>Not Found</h1>
    <p>
    The requested URL <tt>{{ request_path }}</tt> was not found on this server.
    </p>
  </body>
</html>""")
    c = Context({'request_path': request.path})
    return HttpResponseNotFound(t.render(c))

def handler500(request):
    return HttpResponseServerError("""\
<html>
  <head>
    <title>500 Internal Server Error</title>
  </head>
  <body>
    <h1>Internal Server Error</h1>
    <p>The server encountered a problem while trying to fulfill your
    request. Please try again later.</p>
  </body>
</html>""")

urlpatterns = patterns('',
    # Some day this will be a general-purpose URL shortener

    (ur'^(?P<sparkblocks>[▁▂▃▅▆▇]+)$',
            lambda request, sparkblocks: redirect_to(request,
                url='https://datacollective.org/' + sparkblocks,
                permanent=False)),
    (ur'^$', redirect_to, {
        'url': 'https://datacollective.org/sparkblocks.html',
        'permanent': False}),
    (r'^header_image.jpg$', redirect_to, {
        'url': 'http://d4t4.org/static/header_image.jpg',
        'permanent': False}),
)
