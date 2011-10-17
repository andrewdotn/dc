# coding: UTF-8

import json
import os
import pkg_resources
import subprocess
import sys
import tempfile

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import (HttpResponse, Http404, HttpResponseServerError,
    HttpResponseForbidden)
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt

from chart import utils
from chart.models import Chart
from settings.common import VENDOR_ROOT

def index(request):
    charts = Chart.objects.all().select_related('creator')
    return render(request, 'chart/index.html', {'charts': charts})

def charts_by_user(request, username):
    try:
      user = get_object_or_404(User, username = username)
    except Http404:
      raise Http404("The user '%s' does not exist." % username)
    charts = Chart.objects.filter(creator__exact = user).select_related(
            'creator')
    return render(request, 'chart/index.html',
        {'charts': charts, 'for_user': user})

def unicode_problem_debug(request, s):
    if s:
        raise Http404("‘hi’")
    raise Http404(u"‘uhi’")

def sparklink(request, sparkblocks):
    chart = get_object_or_404(Chart, sparkblocks=sparkblocks)
    return view(request, chart=chart)

def view(request, chart_id, title=None):
    chart = get_object_or_404(Chart, id=chart_id)
    if chart.slug_title() and title != chart.slug_title():
        return redirect(chart.get_absolute_url())
    return render(request, 'chart/chart.html', {
        'chart': chart,
        'host': request.get_host(),
        'chart_data': chart.chart_data.replace('\r\n', '\\n').replace('\n', '\\n').replace('\r', '\\n'),
        'chart_settings': mark_safe(chart.chart_settings.replace('\n', ' ').replace('\r', ' ')),
        'enclosing_width': chart.enclosing_width(request.GET.get("width", None)),
    })

# TODO Error handling would be nice.

@user_passes_test(lambda u: u.is_active)
def new(request):
    if request.POST:
        data = request.POST["data"]

        try:
            chart_data = utils.import_chart_data(data)
        except Exception, e:
            utils.save_import_failure(request.user.username, data)
            return HttpResponseServerError('Parse error: ' + e.message)

        chart = Chart(creator=request.user)
        chart.chart_data = chart_data
        chart.save()

        return redirect(reverse('chart.views.edit', args=[chart.id]))
    else:
        return render(request, 'chart/new.html')

def image(request, chart_id=None):
    chart = get_object_or_404(Chart, id=chart_id)
    try:
        with open(utils.chart_image_path(chart.id), "rb") as f:
            image_data = f.read()
    except IOError:
        raise Http404

    return HttpResponse(image_data, mimetype="image/png")

# TODO Queue conversion requests.
# TODO Handle csrf issues when this becomes an Ajax request.

BATIK_JAR_PATH = os.path.join(VENDOR_ROOT, "batik", "batik-rasterizer.jar")

@csrf_exempt
@user_passes_test(lambda u: u.is_staff)
def convert(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)

    # Output svg data.

    f, svg_path = tempfile.mkstemp()
    png_path = utils.chart_image_path(chart_id)

    with os.fdopen(f, "wb") as fd:
        fd.write(request.POST["svg"])

    # Convert to png.

    status = subprocess.check_call(
        ["java", "-Xmx10m", "-Djava.awt.headless=true",
        "-jar", BATIK_JAR_PATH, "-d", png_path, svg_path])

    # For debug purposes, if we were asked for svg, save the svg data as well.  Otherwise delete it.

    if request.POST["type"] == "image/svg+xml":
        os.rename(svg_path, utils.chart_image_path(chart_id, ext="svg"))
    else:
        os.remove(svg_path)

    return image(request, chart_id)

def embed(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)

    return render(request, 'chart/embed.html', {
      'host': request.get_host(),
      'url': 'https://%s%s' % (request.get_host(), chart.get_absolute_url()),
      'shorturl': 'https://%s%s' % (request.get_host(),
            reverse('chart.views.view', args=[chart.id])),
      'chart': chart,
      'internal': bool(request.GET.get("internal", False)),
      'source_width': chart.source_width(request.GET.get("width", None)),
      'funtext':['term paper', 'love letter', 'op-ed', 'manifesto']
# is there a way to put funtext into the template where it belongs?
    })

EASYXDM = pkg_resources.resource_string('vendor.easyxdm', 'static/easyxdm/easyXDM.js')

def embed_js(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)


    params = {}
    internal = request.GET.get('internal', False)
    if internal:
        params['internal'] = '1'
    width = request.GET.get('width', None)
    if width:
        params['width'] = width

    chart_url = "https://%s/%s?%s" % (request.get_host(),
            reverse('chart.views.embed', args=[chart.id]), urlencode(params))

    return render(request, 'chart/embed.js', {
      'easyxdm': EASYXDM,
      'chart': chart,
      'chart_url': chart_url,
      'internal': internal,
      'width': width,
    })

@user_passes_test(lambda u: u.is_active)
def edit(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)
    return render(request, 'chart/edit.html', {'chart': chart})

@csrf_exempt
@user_passes_test(lambda u: u.is_active)
def update(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)
    dict = json.loads(request.raw_post_data)

    if dict.has_key('chart_title'):
        chart.title = dict['chart_title']
    if dict.has_key('chart_html_below_title'):
        chart.html_below_title = dict['chart_html_below_title']
    if dict.has_key('chart_y_axis_description'):
        chart.y_axis_description = dict['chart_y_axis_description']
    if dict.has_key('chart_source_title'):
        chart.source_title = dict['chart_source_title']
    if dict.has_key('chart_settings'):
        chart.chart_settings = json.dumps(dict['chart_settings'])
    if dict.has_key('chart_data'):
        chart.chart_data = json.dumps(dict['chart_data'])
    if dict.has_key('chart_width'):
        chart.chart_width = json.dumps(dict['chart_width'])
    if (request.user == chart.creator) or request.user.is_superuser:
        chart.save()
        return HttpResponse('ok')
    else:
        return HttpResponseForbidden('Permission denied.')

@csrf_exempt
@user_passes_test(lambda u: u.is_active)
def convert_data(request):
    try:
        dict = json.loads(request.raw_post_data)
        chart_data = utils.import_chart_data(dict['data'])
        json_data = json.dumps(chart_data)
        return HttpResponse(json_data)
    except Exception:
        utils.save_import_failure(request.user.username, dict['data'])
        raise

@user_passes_test(lambda u: u.is_staff)
def fivehundred(request):
    return render(request, 'chart/noexist', {
      'bah': foo
    })
