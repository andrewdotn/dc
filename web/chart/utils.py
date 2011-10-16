# coding: UTF-8

import csv
import os
import tempfile

from django.conf import settings

def chart_image_path(chart_id, ext="png"):
    return os.path.join(settings.DATA_DIR, "images", "{0}.{1}".format(chart_id, ext))

def import_chart_data(data):
    # Sanitize line endings and split into lines.

    lines = data.strip().replace('\r\n', '\n').split('\n')

    # Use tab for delimiter if it exists in the data; otherwise assume comma.

    delimiter = '\t'
    if not delimiter in data:
        delimiter = ','

    # Load csv in the format:
    #   name1  name2  name3
    #       1      2      3
    #       4      5      6
    # Zip to get each column into its own array.

    reader = csv.reader(lines, delimiter=delimiter)

    series_list = zip(*[value for value in reader])

    # Create a series dict for each column.

    chart_data = []

    for series in series_list:
        dict = {
            'name': series[0],
            'data': [float(value.replace(',', '')) for value in series[1:]]
        }
        chart_data.append(dict)

    return chart_data

def save_import_failure(username, data):
    dir = os.path.join(settings.DATA_DIR, "imports", "failures")
    f, path = tempfile.mkstemp(dir=dir, prefix=(username+"-"), suffix=".txt")

    with os.fdopen(f, "wb") as fd:
        fd.write(data)
