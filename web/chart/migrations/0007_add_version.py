# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Chart.version'
        db.add_column('chart_chart', 'version', self.gf('django.db.models.fields.PositiveIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Chart.version'
        db.delete_column('chart_chart', 'version')


    models = {
        'chart.chart': {
            'Meta': {'object_name': 'Chart'},
            'chart_creator': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'chart_creator_avatar': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'chart_creator_detail': ('django.db.models.fields.TextField', [], {}),
            'chart_data': ('django.db.models.fields.TextField', [], {}),
            'chart_settings': ('django.db.models.fields.TextField', [], {}),
            'csv_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'disqus_identifier': ('django.db.models.fields.TextField', [], {'max_length': '20'}),
            'html_below_title': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source_detail': ('django.db.models.fields.TextField', [], {}),
            'source_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'sparkblocks': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'version': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'xls_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'y_axis_description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['chart']
