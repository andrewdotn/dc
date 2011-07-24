from django.db import models

class PageSet(models.Model):
    name = models.CharField(max_length=30)
    template_name = models.CharField(max_length=30)

class Page(models.Model):
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=80)
    filename = models.CharField(max_length=30, unique=True)
    content = models.TextField()
    order = models.IntegerField()
    pageset = models.ForeignKey(PageSet)
