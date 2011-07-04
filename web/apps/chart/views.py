from django.shortcuts import render_to_response, get_object_or_404
from django.utils.safestring import mark_safe

from chart.models import Chart

def index(request):
    charts = Chart.objects.all()
    return render_to_response('chart/index.html',
        {'charts': charts})

def sparklink(request, sparkblocks):
    chart = get_object_or_404(Chart, sparkblocks=sparkblocks)
    return view(request, chart=chart)

# XXX admin needs this
def view(request, chart_id=None, chart=None):
    if chart is None:
        chart = get_object_or_404(Chart, id=chart_id)
    return render_to_response('chart/chart.html', {
        'chart': chart,
        'url': 'http://d4t4.org/' + chart.sparkblocks,
        'shorturl': 'http://d4t4.org/' + chart.sparkblocks,
        'chart_data': chart.chart_data.replace('\n', r'\n'),
        'chart_settings': mark_safe(chart.chart_settings.replace('\n', ' ').replace('\r', ' ')),
    })
