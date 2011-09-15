#!/usr/bin/env python2.7

import argparse
import locale
import os.path
import sys

from django.core.management import ManagementUtility

if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding(locale.getpreferredencoding().lower())

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

PROG = os.path.basename(__file__)

parser = argparse.ArgumentParser(add_help=False)
group = parser.add_mutually_exclusive_group()
group.add_argument('--d4t4', action='store_const', dest='site', const='d4t4')
group.add_argument('--dc', action='store_const', dest='site', const='dc')

group = parser.add_mutually_exclusive_group()
group.add_argument('--dev', action='store_const', dest='realm', const='dev')
group.add_argument('--prod', action='store_const', dest='realm', const='prod')
group.add_argument('--staging', action='store_const', dest='realm',
        const='staging')

if '--help' in sys.argv or 'help' in sys.argv:
    print """Usage: %(prog)s [--d4t4 | --dc] ARGS...

This is a wrapper around %(prog)s that allows selecting which site to
manage. ARGS are as described below.
""" % { 'prog': PROG }

options, args = parser.parse_known_args()
if options.site is None:
    options.site = 'd4t4'

if options.realm is None:
    options.realm = 'dev'

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.%s_%s' % (
        options.site, options.realm)

utility = ManagementUtility([sys.argv[0]] + args)
utility.execute()
