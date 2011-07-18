# coding: UTF-8

import re

from django.core.management.base import NoArgsCommand
from django.conf import settings

RE_SETTING = re.compile('^[A-Z0-9_]+$')
RE_BUILTIN = re.compile('^__[a-z_]+__$')

class Command(NoArgsCommand):
    help = 'Display this installation’s settings.'

    def handle_noargs(self, **options):
        skipped = set()

        for k in sorted(dir(settings)):
            if RE_SETTING.match(k):
                print >> self.stdout, k, '=', repr(getattr(settings, k))
            elif not RE_BUILTIN.match(k):
                skipped.add(k)
        if skipped:
            print >> self.stdout, '(Skipped', ', '.join(skipped) + ')'
