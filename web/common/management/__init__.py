# coding: UTF-8

import getpass
import subprocess
import sys

from django.core.management.base import CommandError

def is_development_environment():
    """Return True if this seems safe to run development commands, such as
    creating a test user with a well-known password."""

    try:
        ensure_development()
    except:
        return False

def ensure_development():
    "Raise an exception if not in a development environment."

    def abort_not_development(msg):
        raise CommandError(
            'This doesn’t seem like a development configuration: ' + msg)

    if 'd4t4' in getpass.getuser():
        abort_not_development('‘d4t4’ is in the user name.')

    if sys.platform != 'darwin':
        # darwin hostname has no --fqdn option, but darwin is presumably
        # not a server
        if 'dreamhost' in subprocess.check_output(['hostname', '--fqdn']):
            abort_not_development('You’re on dreamhost.')
