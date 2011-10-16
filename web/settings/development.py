# coding: UTF-8

import os.path

from common import *

DEBUG = True

## Uncomment to enable toolbar debugging of non-debug servers
#DEBUG_TOOLBAR_CONFIG = {
#    'SHOW_TOOLBAR_CALLBACK':
#        lambda r: r.META.get('REMOTE_ADDR', None) == '127.0.0.1'
#}

TEMPLATE_DEBUG = DEBUG

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

def enable_toolbar():
    global MIDDLEWARE_CLASSES
    global INSTALLED_APPS
    MIDDLEWARE_CLASSES.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
    INSTALLED_APPS.append('debug_toolbar')

MIDDLEWARE_CLASSES.insert(0,
    'common.middleware.ServePublicInDevelopmentMiddleware')

# Uncomment to log queries; add UseDebugCursorMiddleware if DEBUG is not set
#
# LOGGING['loggers']['django.db.backends'] = {
#     'handlers': ['console'],
#     'level': 'DEBUG',
# }
