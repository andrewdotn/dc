# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Adding model 'PageSet'
        db.create_table('pageset_pageset', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('template_name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal('pageset', ['PageSet'])

        # Adding model 'Page'
        db.create_table('pageset_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('short_title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('filename', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('pageset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pageset.PageSet'])),
        ))
        db.send_create_signal('pageset', ['Page'])


    def backwards(self, orm):
        
        # Deleting model 'PageSet'
        db.delete_table('pageset_pageset')

        # Deleting model 'Page'
        db.delete_table('pageset_page')


    models = {
        'pageset.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'pageset': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['pageset.PageSet']"}),
            'short_title': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'pageset.pageset': {
            'Meta': {'object_name': 'PageSet'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['pageset']
