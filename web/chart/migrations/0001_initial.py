# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Chart'
        db.create_table('chart_chart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sparkblocks', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('tweet', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('source_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('source_title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('source_detail', self.gf('django.db.models.fields.TextField')()),
            ('chart_creator', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('chart_creator_avatar', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('chart_creator_detail', self.gf('django.db.models.fields.TextField')()),
            ('disqus_identifier', self.gf('django.db.models.fields.TextField')(max_length=20)),
            ('chart_data', self.gf('django.db.models.fields.TextField')()),
            ('chart_settings', self.gf('django.db.models.fields.TextField')()),
            ('csv_url', self.gf('django.db.models.fields.URLField')(default=None, max_length=200)),
            ('xls_url', self.gf('django.db.models.fields.URLField')(default=None, max_length=200)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=255))

        ))
        db.send_create_signal('chart', ['Chart'])


    def backwards(self, orm):
        
        # Deleting model 'Chart'
        db.delete_table('chart_chart')


    models = {
        'chart.chart': {
            'Meta': {'object_name': 'Chart'},
            'chart_creator': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'chart_creator_avatar': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'chart_creator_detail': ('django.db.models.fields.TextField', [], {}),
            'chart_data': ('django.db.models.fields.TextField', [], {}),
            'chart_settings': ('django.db.models.fields.TextField', [], {}),
            'disqus_identifier': ('django.db.models.fields.TextField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'source_detail': ('django.db.models.fields.TextField', [], {}),
            'source_title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'sparkblocks': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tweet': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'csv_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'xls_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['chart']
