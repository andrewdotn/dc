# coding: UTF-8

import csv
import os
import tempfile
import re
import json

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

    x_series = series_list[0]
    series_list = series_list[1:]
    chart_data = []
        
    for series in series_list:
        series_name = series[0]

        the_data = []
        for index in range(1, len(series)):
            the_y_value = float(series[index].replace(',', ''))
            the_x_value = int(x_series[index])
            the_data.append([the_x_value,the_y_value])

        dict = {
            'name': series_name,
            'data': the_data
        }
        chart_data.append(dict)


    return chart_data

def save_import_failure(username, data):
    dir = os.path.join(settings.DATA_DIR, "imports", "failures")
    f, path = tempfile.mkstemp(dir=dir, prefix=(username+"-"), suffix=".txt")

    with os.fdopen(f, "wb") as fd:
        fd.write(data)
