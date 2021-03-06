# coding: UTF-8

import sys

from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def handler404(request):
    d = {
        'request_path': request.path,
        'referer': request.META.get('HTTP_REFERER', '')
    }
    t, e, traceback = sys.exc_info()
    if t == Http404:
        d['exception'] = e
    return render(request, '404.html', d, status=404)

@requires_csrf_token
def handler500(request):
    d = {
        'request_path': request.path
    }
    return render(request, '500.html', d, status=500)
