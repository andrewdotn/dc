# coding: UTF-8

import os.path

from common import *

DEBUG = True
TEMPLATE_DEBUG = False

# 127.0.0.1 can’t be trusted on a shared host
INTERNAL_IPS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'OPTIONS': {
            'read_default_file': os.path.expanduser('~/.my.cnf'),
        }
    }
}
