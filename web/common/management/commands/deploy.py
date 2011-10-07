# coding: UTF-8

import subprocess
import sys

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError
from django.db import connection

from .. import ensure_development

class Command(NoArgsCommand):
    help = 'Deploy latest code in bitbucket to production'

    def handle_noargs(self, **options):
        ensure_development()

        subprocess.call(["ssh", "d4t4.org", "dc/scripts/deploy"])
