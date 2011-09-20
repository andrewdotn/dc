import os
import pkg_resources
import subprocess
import tempfile

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test

from chart import utils
from settings.common import VENDOR_ROOT

from chart.models import Chart

def index(request):
    charts = Chart.objects.all()
    return render(request, 'chart/index.html', {'charts': charts})

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
    })

def image(request, chart_id=None, short_name=None):
    chart = get_chart(chart_id, short_name)
    image_data = open(utils.chart_image_path(chart.id), "rb").read()
    return HttpResponse(image_data, mimetype="image/png")

# TODO Queue conversion requests.
# TODO Handle csrf issues when this becomes an Ajax request.

BATIK_JAR_PATH = os.path.join(VENDOR_ROOT, "batik", "batik-rasterizer.jar")

@csrf_exempt
@user_passes_test(lambda u: u.username == 'admin')
def convert(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)

    f, svg_path = tempfile.mkstemp()
    png_path = utils.chart_image_path(chart_id)

    fd = os.fdopen(f, "w")
    fd.write(request.POST["svg"])
    fd.close()

    status = subprocess.call(["java", "-jar", BATIK_JAR_PATH, "-d", png_path, svg_path])

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
      'url': '//' + request.get_host() + '/chart/' + chart.short_name,
      'chart': chart,
      'internal': bool(request.GET.get("internal", False)),
      'funtext':['term paper', 'love letter', 'op-ed', 'manifesto']
# is there a way to put funtext into the template where it belongs?
    })

EASYXDM = pkg_resources.resource_string('vendor.easyxdm', 'static/easyxdm/easyXDM.js')

def embed_js(request, chart_id):
    chart = get_object_or_404(Chart, id=chart_id)

    chart_url = "https://" + request.get_host() + "/chart/embed/" + str(chart.id)
    if request.GET.get("internal", False):
        chart_url += "?internal=1"

    return render(request, 'chart/embed.js', {
      'easyxdm': EASYXDM,
      'chart': chart,
      'chart_url': chart_url,
      'internal': bool(request.GET.get("internal", False))
    })
