from django.template import Context, Template, Library
from django.conf import settings
from django.template.defaultfilters import stringfilter

register = Library()

@register.filter
@stringfilter
def split(value, delimiter=None):
    "str.split"
    if delimiter is None:
        return value.split()
    return value.split(delimiter)
