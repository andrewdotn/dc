# coding: UTF-8

import os
import os.path
import sys
import json

# All keys in ~/.dc_secrets.json are loaded into this module. If the file
# doesn’t exist, it’s created with sane defaults.

secret_file = os.path.expanduser('~/.dc_secrets.json')

if not os.path.isfile(secret_file):
    old_umask = os.umask(0077)
    try:
        with open(secret_file, 'w') as secrets:
            import string
            from random import choice
            secret_key = ''.join([choice(
                    string.letters + string.digits + string.punctuation)
                    for i in range(50)])
            json.dump({'SECRET_KEY': secret_key}, secrets, indent=2)
            secrets.write('\n')
    finally:
        os.umask(old_umask)

with open(secret_file) as secrets:
    stuff = json.load(secrets)
    for k, v in stuff.items():
        # json returns unicode objects, but module definitions are strs.
        setattr(sys.modules[__name__], k.encode('UTF-8'), v.encode('UTF-8'))

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

ADMINS = (
    ('Data Collective Webmaster', 'webmaster@datacollective.org'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)

# Python timezone handling is problematic, just use UTC
TIME_ZONE = 'UTC'

# TODO: DATE_FORMAT &c.

# English only for now

LANGUAGE_CODE = 'en-us'

LANGUAGES = (('en', 'English'),)

USE_I18N = False

USE_L10N = False

# defaults for South

SKIP_SOUTH_TESTS = False

SOUTH_TESTS_MIGRATE = True

# currently only used by runservers command
SITES = [
    {'name': 'dc'},
    {'name': 'd4t4'},
]

SITE_ID = 1

STATIC_ROOT = os.path.join(BASE_DIR, 'public', 'static')

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

MIDDLEWARE_CLASSES = (
    #'common.middleware.UseDebugCursorMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'south',
    'debug_toolbar',

    'vendor.amcharts',
    'vendor.highcharts',

    'common',
    'chart',
    'pageset'
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
