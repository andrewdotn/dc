# coding: UTF-8

import os
import subprocess
import sys

from django.conf import settings
from django.contrib.auth.models import User
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError
from django.db import connection

from .. import ensure_development

class Command(NoArgsCommand):
    help = 'Display this installation’s settings.'

    def handle_noargs(self, **options):
        ensure_development()

        from django.conf import settings

        os.chdir(settings.BASE_DIR)
        subprocess.check_call(['hg', 'pull'])
        subprocess.check_call(['hg', 'update'])

        os.chdir('vendor')

        subprocess.check_call(['hg', 'pull'])
        subprocess.check_call(['hg', 'update'])

        os.chdir(settings.BASE_DIR)

        subprocess.check_call(['pip', 'install', '-r', '../requirements.txt'])

        subprocess.check_call(['./manage.py']
            + settings.MANAGEMENT_COMMAND_ARGUMENTS
            + ['syncdb', '--migrate'])
