# coding: UTF-8

import re
import select
import subprocess
import sys

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

RE_ANSI_COLOUR = re.compile(r'^(%s\[[0-9;]*m)+' % '\x1b')

# In the future this will also set up the site definitions in the database
# correctly too.

class Command(BaseCommand):
    help = 'Run development servers for all sites.'
    args = '[starting port number]'

    def handle(self, start_port='', *args, **options):
        if args:
            raise CommandError('Usage is runservers %s' % self.args)

        if not start_port:
            start_port = 8000

        try:
            port = int(start_port)
        except ValueError:
            raise CommandError('%s is not a valid port number.' % start_port)

        from common.management.commands.runsslserver import generate_certificate
        generate_certificate()

        try:
            processes = []
            fds = []
            label = {}
            for site in settings.SITES:
                p = subprocess.Popen(['./manage.py', '--' + site['name']]
                        + settings.MANAGEMENT_COMMAND_ARGUMENTS
                        + ['runsslserver', str(port)],
                    stderr=subprocess.PIPE, bufsize=1)
                port += 1
                processes.append(p)
                fds.append(p.stderr)
                label[p.stderr] = site['name']

            # prefix request log lines with site names
            while all(p.poll() is None for p in processes):
                r_ready, w_ready, x_ready = select.select(fds, [], [])

                for fd in r_ready:
                    colour = ''
                    line = fd.readline()
                    match = RE_ANSI_COLOUR.match(line)
                    if match:
                        colour = match.group()
                        line = line[match.end():]
                    if line:
                        print >> sys.stderr, '%s%4s %s' % (
                                colour, label[fd], line),
        except KeyboardInterrupt:
            pass
        finally:
            for p in processes:
                try:
                    if p.poll() is not None:
                        p.terminate()
                except OSError:
                    pass
