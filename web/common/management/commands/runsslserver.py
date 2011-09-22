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

    # Literal s/http/https/ of program text from core_command. This is done
    # so that the run() call in this method refers to this module
    def inner_run(self, *args, **options):
        from django.conf import settings
        from django.utils import translation

        shutdown_message = options.get('shutdown_message', '')
        quit_command = (sys.platform == 'win32') and 'CTRL-BREAK' or 'CONTROL-C'

        self.stdout.write("Validating models...\n\n")
        self.validate(display_num_errors=True)
        self.stdout.write((
            "Django version %(version)s, using settings %(settings)r\n"
            "Development server is running at https://%(addr)s:%(port)s/\n"
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

def generate_certificate(force=False):
    """Return the filename of a self-signed certificate for localhost,
    generating one if one doesn’t already exist or if force is True."""

    from django.conf import settings
    certfile = os.path.join(settings.BASE_DIR, 'localhost.pem')

    if force or not os.path.isfile(certfile):
        print >> sys.stderr, "Generating an SSL certificate for you.\n"

        try:
            conf_file_name = 'openssl.cnf'
            with open(conf_file_name, 'w') as conf_file:
                conf_file.write("""\
[ req ]
x509_extensions        = v3_ca
distinguished_name      = req_distinguished_name

[ req_distinguished_name ]
commonName = localhost

[ v3_ca ]
basicConstraints = critical,CA:FALSE
nsCertType = server
keyUsage = digitalSignature, keyEncipherment, keyCertSign
extendedKeyUsage = critical,serverAuth
subjectAltName = DNS:localhost,DNS:local.host""")

            subprocess.check_call(['openssl', 'req', '-config', conf_file_name,
                '-extensions', 'v3_ca', '-x509', '-new', '-days', '365',
                '-subj', '/O=Auto-Generated Development Certificate Authority',
                '-nodes', '-out', certfile, '-keyout', certfile])

        finally:
            os.unlink(conf_file_name)

        if sys.platform == 'darwin':
            try:

                print >> sys.stderr, """
To make debugging SSL lock icon issues easier, I’m going to have you mark
the certificate I just created as trusted by entering your password now. If
you don’t want to do this, just press cancel.
"""

                pem_file = certfile + '.pem'
                der_file = certfile + '.der'

                subprocess.check_call(['openssl', 'x509', '-in', certfile,
                        '-outform', 'pem', '-out', pem_file])
                subprocess.check_call(['openssl', 'x509', '-in', certfile,
                        '-outform', 'der', '-out', der_file])

                subprocess.check_call(['security', 'add-certificates', der_file])
                subprocess.check_call(['security',
                        'add-trusted-cert', '-p', 'ssl', '-p', 'basic', pem_file])

            except Exception:
                print >> sys.stderr, """
That failed. I’m assuming you cancelled, and am carrying on.
Erase %s to try again.""" % certfile

            finally:
                os.unlink(pem_file)
                os.unlink(der_file)

            print >> sys.stderr, """Great!\n"""

            found = False
            with open('/etc/hosts', 'r') as hosts:
                for line in hosts:
                    if not line.strip().startswith('#'):
                        parts = line.split()
                        if len(parts) >= 2:
                            if parts[1] == 'local.host':
                                found = True
                                break
            if not found:
                print >> sys.stderr, """\
One last step: I’m going to add local.host as an alias for 127.0.0.1 in
your /etc/hosts. You’ll then access the site via https://local.host:port/.
This is necessary for a green lock icon in Chrome. So that’s what’s going
on if you get a password prompt now.
"""

                try:
                    subprocess.check_call(['sudo', 'sh', '-c',
                            'echo "127.0.0.1 local.host" >> /etc/hosts'])
                except Exception:
                    print >> sys.stderr, \
                            "That didn’t work. Please edit /etc/hosts manually."

    return certfile

def run(addr, port, wsgi_handler, ipv6=False):
    server_address = (addr, port)
    httpd = WSGISSLServer(generate_certificate(), server_address,
        WSGIRequestHandler, ipv6=ipv6)
    httpd.set_app(wsgi_handler)
    httpd.serve_forever()
