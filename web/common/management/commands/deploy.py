# coding: UTF-8

import subprocess
import sys

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError
from django.db import connection

def abort_not_development(msg):
    raise CommandError('This doesn’t seem like a development configuration: '
                       + msg)

class Command(NoArgsCommand):
    help = 'Deploy latest code in bitbucket to production'

    def handle_noargs(self, **options):
        if not settings.DEBUG:
            abort_not_development('DEBUG is not set.')
        if connection.vendor != 'sqlite':
            abort_not_development('DB vendor is not sqlite.')

        subprocess.call(["ssh", "d4t4.org", "deploy"])
