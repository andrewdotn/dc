# coding: UTF-8

import os.path

from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.db import connection
from django.http import Http404
from django.views import static

class UseDebugCursorMiddleware(object):
    def __init__(self):
        connection.use_debug_cursor = True
        raise MiddlewareNotUsed()

class ServePublicInDevelopmentMiddleware(object):
    """Mimic passenger’s serving of files from ‘public’ in development.

    Before calling any other handlers, check if it’s a request for a file
    on disk, and serve it if so."""

    def __init__(self):
        if not settings.DEBUG:
            raise MiddlewareNotUsed()
        print 'hi'

    def process_request(self, request):
        try:
            return static.serve(request, request.META['PATH_INFO'],
                document_root=os.path.join(settings.BASE_DIR, 'public'))
        except Http404:
            return None
