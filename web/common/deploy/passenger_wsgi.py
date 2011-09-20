#!/usr/bin/env python2.5
# coding: UTF-8

import os
import os.path
import sys
import time
import traceback

if sys.version < "2.7":
  python = os.path.join(os.environ['HOME'], 'local', 'bin', 'python2.7')
  os.execl(python, python, *sys.argv)

# On linux, toggle this to find out where stdout and stderr logs are going.
# stdout is fd 1
# stderr is fd 2
if False:
    log = open(os.path.expanduser('~/log.log'), 'w')
    for fd in os.listdir('/proc/self/fd'):
        try:
            target = os.readlink('/proc/self/fd/' + fd)
            print >> log, '%3s' % fd, target
        except Exception:
            print >> log, '%3s' % fd, '[gone]'
    log.close()

if hasattr(sys, 'setdefaultencoding'):
    sys.setdefaultencoding(locale.getpreferredencoding().lower())

import django.core.handlers.wsgi
sys.path.insert(0, os.path.join(os.getcwd(), 'dc/web'))

os.environ['DJANGO_SETTINGS_MODULE'] = "settings.d4t4_prod"

def application(environ, start_response):
    try:
        handler = django.core.handlers.wsgi.WSGIHandler()
        return handler(environ, start_response)
    except Exception, e:
        errlog = open(os.path.join(os.getcwd(), 'error.log'), 'a')
        try:
          errlog.write(time.strftime("%Y-%m-%d %H:%M:%S %z: 500: "))
          traceback.print_exc(file=errlog)
        finally:
          errlog.close()

    start_response('500 Internal server error',
         [('Content-type', 'text/plain; charset=UTF-8')])
    return ["Something went wrong, we’re looking into it."]
