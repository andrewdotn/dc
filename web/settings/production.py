# coding: UTF-8

import os.path

from common import *

DEBUG = False
TEMPLATE_DEBUG = False

# 127.0.0.1 can’t be trusted on a shared host
INTERNAL_IPS = []

DATA_DIR = os.path.expanduser("~/data")

SENTRY_URL_PREFIX = 'https://datacollective.org/'

STATIC_URL = 'https://d9zwdpgl8r5wd.cloudfront.net/'

# Cache compiled templates. Requires all template tags to be thread-safe.
# https://docs.djangoproject.com/en/1.3/howto/custom-template-tags/#template-tag-thread-safety
TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )),
)
