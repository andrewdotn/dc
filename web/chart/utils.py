import os

from settings.common import BASE_DIR

def chart_image_path(chart_id, ext="png"):
    return os.path.join(BASE_DIR, "data", "images", "{0}.{1}".format(chart_id, ext))
