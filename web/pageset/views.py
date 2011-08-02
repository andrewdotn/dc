from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from .models import Page, PageSet

def byfilename(request, filename, pageset_name):
    pageset = get_object_or_404(PageSet, name=pageset_name)
    page = get_object_or_404(Page, filename=filename, pageset=pageset)
    other_pages = list(pageset.page_set.values('title', 'short_title',
            'filename', 'order'))
    other_pages.sort(key=lambda x: -x['order'])

    return render(request, pageset.template_name,
            {'pages': other_pages, 'page': page})
