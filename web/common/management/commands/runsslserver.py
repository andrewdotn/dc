# coding: UTF-8

import os
import os.path
import ssl
import subprocess
import sys
import traceback
from SocketServer import TCPServer

from django.core.servers.basehttp import AdminMediaHandler, WSGIServerException, WSGIServer, WSGIRequestHandler

from django.contrib.staticfiles.management.commands.runserver \
        import Command as static_command
from django.core.management.commands.runserver \
        import Command as core_command

# static_command extends core_command by adding some options and wrapping
# get_handler. It comes first in the inheritance order so that its
# overridden methods get called.
class Command(static_command, core_command):

    # XXX This should only be set if the server is actually running, but I
    # can’t find a later place to run it that still works.
    os.environ['HTTPS'] = 'on'

    # literal copy-and-paste of program text from core_command so that
    # run() refers to this module
    def inner_run(self, *args, **options):
        from django.conf import settings
        from django.utils import translation

        shutdown_message = options.get('shutdown_message', '')
        quit_command = (sys.platform == 'win32') and 'CTRL-BREAK' or 'CONTROL-C'

        self.stdout.write("Validating models...\n\n")
        self.validate(display_num_errors=True)
        self.stdout.write((
            "Django version %(version)s, using settings %(settings)r\n"
            "Development server is running at http://%(addr)s:%(port)s/\n"
            "Quit the server with %(quit_command)s.\n"
        ) % {
            "version": self.get_version(),
            "settings": settings.SETTINGS_MODULE,
            "addr": self._raw_ipv6 and '[%s]' % self.addr or self.addr,
            "port": self.port,
            "quit_command": quit_command,
        })
        # django.core.management.base forces the locale to en-us. We should
        # set it up correctly for the first request (particularly important
        # in the "--noreload" case).
        translation.activate(settings.LANGUAGE_CODE)

        try:
            handler = self.get_handler(*args, **options)
            run(self.addr, int(self.port), handler, ipv6=self.use_ipv6)
        except WSGIServerException, e:
            # Use helpful error messages instead of ugly tracebacks.
            ERRORS = {
                13: "You don't have permission to access that port.",
                98: "That port is already in use.",
                99: "That IP address can't be assigned-to.",
            }
            try:
                error_text = ERRORS[e.args[0].args[0]]
            except (AttributeError, KeyError):
                error_text = str(e)
            sys.stderr.write(self.style.ERROR("Error: %s" % error_text) + '\n')
            # Need to use an OS exit because sys.exit doesn't work in a thread
            os._exit(1)
        except KeyboardInterrupt:
            if shutdown_message:
                self.stdout.write("%s\n" % shutdown_message)
            sys.exit(0)

# Inherit form object because super doesn’t work with classic classes
class SSLServer(TCPServer, object):
    def __init__(self, certfile, *args, **kwargs):
        self.certfile = certfile
        super(SSLServer, self).__init__(*args, **kwargs)

    def get_request(self):
        try:
            (socket, fromaddr) = self.socket.accept()
            ssl_socket = ssl.wrap_socket(
                    socket, server_side=True, do_handshake_on_connect=True,
                    certfile=self.certfile)
            socket = None
            return (ssl_socket, fromaddr)
        except Exception:
            raise

class WSGISSLServer(SSLServer, WSGIServer):
    pass

def run(addr, port, wsgi_handler, ipv6=False):
    from django.conf import settings
    certfile = os.path.join(settings.BASE_DIR, 'localhost.pem')
    if not os.path.isfile(certfile):
        subprocess.call(['openssl', 'req',
                '-batch',
                '-new', '-x509', '-days', '365', '-nodes',
                '-out', certfile, '-keyout', certfile,
                '-subj', '/CN=localhost'])

    server_address = (addr, port)
    httpd = WSGISSLServer(certfile, server_address,
        WSGIRequestHandler, ipv6=ipv6)
    httpd.set_app(wsgi_handler)
    httpd.serve_forever()
