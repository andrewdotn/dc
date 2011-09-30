# coding: UTF-8

import sys

def check_development():
    def abort_not_development(msg):
        raise CommandError(
            'This doesn’t seem like a development configuration: ' + msg)

    if sys.platform != 'darwin':
        abort_not_development('you’re not on a mac.')
