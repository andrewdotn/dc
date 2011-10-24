# coding: UTF-8

import os
import os.path
import sys
import json
import re

# All keys in ~/.dc_secrets.json are loaded into this module. If the file
# doesn’t exist, it’s created with sane defaults.
#
# Make sure the key name contains the string “SECRET” or “PASSWORD” so that
# it will be masked out in exception reports.

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

BCRYPT_ENABLED = True

BCRYPT_ROUNDS = 9

BCRYPT_MIGRATE = True

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'OPTIONS': {
            'read_default_file': os.path.expanduser('~/.my.cnf'),
        }
    }
}

DATA_DIR = os.path.join(BASE_DIR, "data")

ADMINS = (
    ('Data Collective Webmaster', 'webmaster@datacollective.org'),
)

MANAGERS = ADMINS

SENTRY_ADMINS = ('webmaster@datacollective.org',)

SENTRY_SERVER_EMAIL = 'Sentry <webmaster@datacollective.org>'

# The default root@localhost is blocked by mail servers
SERVER_EMAIL = 'webmaster@datacollective.org'

ANALYTICS_KEY = 'UA-26195907-1'

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

STATIC_ROOT = os.path.join(BASE_DIR, '..', '..', 'public', 'static')

STATIC_URL = '/static/'
CDN_URL = 'https://d9zwdpgl8r5wd.cloudfront.net/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

ADMIN_MEDIA_PREFIX = '/static/admin/'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

VENDOR_ROOT = os.path.join(BASE_DIR, 'vendor')

MIDDLEWARE_CLASSES = [
    #'common.middleware.UseDebugCursorMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'common.middleware.CatchRedirectLoopMiddleware',
#
# sentry can ignore 404s for now
#
#    'sentry.client.middleware.Sentry404CatchMiddleware',
#
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    'common.context_processors.analytics',
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'south',
    'django_bcrypt',
    'sentry',
    'sentry.client',
    'registration',

    'vendor.amcharts',
    'vendor.highcharts',
    'vendor.easyxdm',

    'common',
    'chart',
    'dc',
    'pageset',
]

# After ten years, the activation email is no longer valid. Deal with it.
ACCOUNT_ACTIVATION_DAYS = 3650

DEFAULT_FROM_EMAIL = 'Data Collective <help@datacollective.org>'

# Enabling this setting allows the testing of Sentry exception handler even if Django DEBUG is enabled.
SENTRY_TESTING = True

SEND_BROKEN_LINK_EMAILS = True

# easyxdm is below because:
#
# Cant figure out why were getting requests for easyxdm this rather
# than easyXDM.
#
# To test on OS X: in Disk Utility, choose File -> New -> Blank Disk Image,
# create a case-sensitive partition, mount it and check out the code there.
#
# So let's just ignore the 404s.  Problem solved!
#
# hypersphere because: http://www.webmasterworld.com/webmaster/4312899.htm

IGNORABLE_404_ENDS = ('/robots.txt', '/hypersphere-2010.png', '/easyxdm.js')

IGNORABLE_404_STARTS = ('/apple-touch-icon.',)

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
            'handlers': ['console', 'mail_admins'],
            'level': 'WARNING',
            'propagate': False,
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
