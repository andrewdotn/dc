import json
import os
import pkg_resources
import subprocess
import sys
import tempfile

from django.http import HttpResponse, Http404, HttpResponseServerError
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test

from chart import utils
from settings.common import VENDOR_ROOT

from chart.models import Chart

def index(request):
    charts = Chart.objects.all().select_related('creator')
    return render(request, 'chart/index.html', {'charts': charts})

def about(request):
    return render(request, 'about.html')

def sparkblocks(request):
    return render(request, 'sparkblocks.html')

def sparklink(request, sparkblocks):
    chart = get_object_or_404(Chart, sparkblocks=sparkblocks)
    return view(request, chart=chart)

def get_chart(chart_id=None, short_name=None):
    if chart_id is not None:
        chart = get_object_or_404(Chart, id=chart_id)
    elif short_name is not None:
        chart = get_object_or_404(Chart, short_name=short_name)
    return chart

# XXX admin needs this
def view(request, chart_id=None, chart=None, short_name=None):
    if chart is None:
        chart = get_chart(chart_id, short_name)
    return render(request, 'chart/chart.html', {
        'chart': chart,
        'host': request.get_host(),
        'url': '//' + request.get_host() + '/chart/' + chart.short_name,
        'shorturl': '//' + request.get_host() + '/chart/' + chart.short_name,
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
        except Exception:
            utils.save_import_failure(request.user.username, data)
            return HttpResponseServerError()

        chart = Chart(creator=request.user)
        chart.chart_data = chart_data
        chart.save()

        return redirect('/chart/edit/{0}/'.format(chart.id))
    else:
        return render(request, 'chart/new.html')

def image(request, chart_id=None, short_name=None):
    chart = get_chart(chart_id, short_name)
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

    try:
        with os.fdopen(f, "wb") as fd:
            fd.write(request.POST["svg"])
    except IOError:
        return HttpResponseServerError()

    # Convert to png.

    status = subprocess.call(["java", "-Xmx10m", "-Djava.awt.headless=true", "-jar", BATIK_JAR_PATH, "-d", png_path, svg_path])

    if status != 0:
        return HttpResponseServerError()

    # For debug purposes, if we were asked for svg, save the svg data as well.  Otherwise delete it.

    try:
        if request.POST["type"] == "image/svg+xml":
            os.rename(svg_path, utils.chart_image_path(chart_id, ext="svg"))
        else:
            os.remove(svg_path)
    except OSError:
        return HttpResponseServerError()

    return image(request, chart_id)

def embed(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)

    return render(request, 'chart/embed.html', {
      'host': request.get_host(),
      'url': 'https://' + request.get_host() + '/chart/' + chart.short_name,
      'chart': chart,
      'internal': bool(request.GET.get("internal", False)),
      'source_width': chart.source_width(request.GET.get("width", None)),
      'funtext':['term paper', 'love letter', 'op-ed', 'manifesto']
# is there a way to put funtext into the template where it belongs?
    })

EASYXDM = pkg_resources.resource_string('vendor.easyxdm', 'static/easyxdm/easyXDM.js')

def embed_js(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)

    chart_url = "https://" + request.get_host() + "/chart/embed/" + str(chart.id) + "?foo=1"
    if request.GET.get("internal", False):
        chart_url += "&internal=1"
    if request.GET.get("width", None):
        chart_url += "&width=" + request.GET.get("width")

    return render(request, 'chart/embed.js', {
      'easyxdm': EASYXDM,
      'chart': chart,
      'chart_url': chart_url,
      'width': request.GET.get("width", None),
      'internal': bool(request.GET.get("internal", False))
    })

@user_passes_test(lambda u: u.is_active)
def edit(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)

    return render(request, 'chart/edit.html', {
      'host': request.get_host(),
      'url': '//' + request.get_host() + '/chart/' + chart.short_name,
      'chart': chart
   })

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

    chart.save()

    return HttpResponse('ok')

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

def fivehundred(request):
    return render(request, 'chart/noexist', {
      'bah': foo
    })
