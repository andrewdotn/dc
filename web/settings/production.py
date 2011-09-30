# coding: UTF-8

import os.path

from common import *

DEBUG = False
TEMPLATE_DEBUG = False

# 127.0.0.1 can’t be trusted on a shared host
INTERNAL_IPS = []

DATA_DIR = os.path.expanduser("~/data")

SENTRY_URL_PREFIX = 'https://datacollective.org/staff'
