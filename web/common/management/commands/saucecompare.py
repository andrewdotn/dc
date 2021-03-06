#!/usr/bin/env python2.7

import os
import sys
import webbrowser

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from optparse import OptionParser
from selenium import webdriver

class BrowserTarget(object):

    # browsers: ANDROID, CHROME, FIREFOX, HTMLUNIT, HTMLUNITWITHJS, INTERNETEXPLORER, IPHONE, OPERA
    # platforms: XP, VISTA, LINUX

    def __init__(self, browser, version, platform):
        self.browser = browser
        self.version = version
        self.platform = platform
        self.png = None

    def run(self, url):
        driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities(),
            command_executor=self.executor_url()
        )

        driver.get(url)
        self.png = driver.get_screenshot_as_base64()
        driver.quit()

    def desired_capabilities(self):
        dc = getattr(webdriver.DesiredCapabilities, self.browser)
        if self.version:
            dc['version'] = self.version
        if self.platform:
            dc['platform'] = self.platform

        return dc

    def executor_url(self):
        return "http://{0}:{1}@ondemand.saucelabs.com:80/wd/hub".format(settings.SECRET_SAUCE_USER, settings.SECRET_SAUCE_KEY)

    def __unicode__(self):
        return '{0} {1} on {2}'.format(self.browser, self.version, self.platform)

class HtmlWriter(object):

    STYLESHEET = '''
        <style type="text/css">
          body {background-color: #ddd;}
          h1 {margin: 0px;}
          td {vertical-align: top; padding: 2px; text-align: center; margin: 0px; border-width: 2px;}
        </style>
    '''

    def write(self, url, targets, f):
        f.write('<html><head>{0}</head><body><table>'.format(self.STYLESHEET))

        f.write('<tr>')
        for target in targets:
            f.write('<td><h2>{0}</h2></td>'.format(unicode(target)))
        f.write('</tr>')

        f.write('<tr>')
        for target in targets:
            f.write('<td>')
            if target.png:
                f.write('<img src="data:image/png;base64,{0}" alt="{1}">'.format(target.png, unicode(target)))
            else:
                f.write('(failed)')
            f.write('</td>')
        f.write('</tr>')

        f.write('</table><h1>{0}<h1></body><html>'.format(url))

class Command(BaseCommand):
    args = '<url> [results.html]'
    help = '''Generate an HTML document of browser snapshots for the given URL.
Output is written to saucecompare.html by default.'''

    def handle(self, *args, **options):
        # Parse args.

        if len(args) < 1 or len(args) > 2:
            raise CommandError('Invalid arguments.')

        url = args[0]

        if len(args) == 2:
            html_path = args[1]
        else:
            html_path = 'saucecompare.html'
        html_path = os.path.abspath(html_path)

        # Run browser targets.

        targets = [
            BrowserTarget('INTERNETEXPLORER', '8', 'XP'),
            BrowserTarget('CHROME', '', 'XP'),
            BrowserTarget('INTERNETEXPLORER', '9', 'VISTA'),
            BrowserTarget('FIREFOX', '6', 'VISTA'),
            BrowserTarget('FIREFOX', '3.6', 'LINUX')
        ]

        for target in targets:
            print 'Running {0}...'.format(unicode(target))
            target.run(url)

        # Write and show html output.

        with open(html_path, 'wb') as f:
            HtmlWriter().write(url, targets, f)

        webbrowser.open("file://" + html_path)
