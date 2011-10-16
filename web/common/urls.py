# coding: UTF-8

import sys

from django.http import Http404
from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token

@requires_csrf_token
def handler404(request):
  d = {'request_path': request.path}
  t, e, traceback = sys.exc_info()
  if t == Http404:
    d['exception'] = e
  return render(request, '404.html', d, status=404)
