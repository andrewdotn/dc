from django.core.exceptions import MiddlewareNotUsed
from django.db import connection

class UseDebugCursorMiddleware(object):
    def __init__(self):
        connection.use_debug_cursor = True
        raise MiddlewareNotUsed()
