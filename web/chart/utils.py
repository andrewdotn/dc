import os

from django.conf import settings

def chart_image_path(chart_id, ext="png"):
    return os.path.join(settings.DATA_DIR, "images", "{0}.{1}".format(chart_id, ext))
