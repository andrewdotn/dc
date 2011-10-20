# coding: UTF-8

import os.path

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.db import connection
from django.http import Http404
from django.views import static

from ..management import ensure_development

class UseDebugCursorMiddleware(object):
    def __init__(self):
        connection.use_debug_cursor = True
        raise MiddlewareNotUsed()

class ServePublicInDevelopmentMiddleware(object):
    """Mimic passenger’s serving of files from ‘public’ in development.

    Before calling any other handlers, check if it’s a request for a file
    on disk, and serve it if so."""

    def __init__(self):
        ensure_development()

    def process_request(self, request):
        try:
            return static.serve(request, request.META['PATH_INFO'],
                document_root=os.path.join(settings.BASE_DIR, 'public'))
        except Http404:
            return None

class RedirectLoopException(Exception):
    pass

class CatchRedirectLoopMiddleware(object):
    def process_response(self, request, response):
        if (response.status_code in (301, 302)
                and request.method == 'GET'
                and request.get_full_path() == response['Location']):
            raise RedirectLoopException(request.get_full_path())
        return response
