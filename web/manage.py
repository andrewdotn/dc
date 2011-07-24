#!/usr/bin/env python2.7

import os.path
import sys

from django.core.management import ManagementUtility

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.dc_dev'

if __name__ == "__main__":
    utility = ManagementUtility(sys.argv)
    utility.execute()
