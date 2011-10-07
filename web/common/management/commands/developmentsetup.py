# coding: UTF-8

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

        manage_command = sys.argv[0]

        self.stdout.write('running %s syncdb -v0 --noinput --migrate\n'
                          % manage_command)
        call_command('syncdb', verbosity=0, interactive=False, migrate=True)

        self.stdout.write(('running %s createsuperuser -v0 --noinput '
                           '--username=admin --email=nobody@example.org\n')
                          % manage_command)
        call_command('createsuperuser',
                     verbosity=0,
                     interactive=False,
                     username='admin',
                     email='nobody@example.org')

        admin_user = User.objects.get(username='admin')
        admin_user.set_password('test')
        admin_user.save()
        self.stdout.write('admin’s password set to “test”\n')
        self.stdout.write('now you can run “' + manage_command
                          + ' runserver” to serve the site locally\n')
