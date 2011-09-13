# coding: UTF-8

import os.path

from common import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

def custom_show_toolbar(request):
    return False # toggle this to decide if we want toolbar or not

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'database.sqlite3'),
    }
}

# Uncomment to log queries; add UseDebugCursorMiddleware if DEBUG is not set
#
# LOGGING['loggers']['django.db.backends'] = {
#     'handlers': ['console'],
#     'level': 'DEBUG',
# }
