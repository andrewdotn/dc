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

@register.filter
def user_display_name(user):
    "Return a human-readable name for a contrib.auth.user object."
    # this should be a method on User, but we want to avoid forking that
    if user.first_name:
        return user.get_full_name()
    return user.username
