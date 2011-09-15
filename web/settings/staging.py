# coding: UTF-8

import os.path

from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',

        'OPTIONS': {
            'read_default_file': os.path.expanduser('~/.my.cnf'),
        }
    }
}
