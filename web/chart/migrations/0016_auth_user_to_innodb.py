# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import connection
from django.db import models

class Migration(SchemaMigration):

    no_dry_run = True

    def forwards(self, orm):
        # Converting auth_user to innodb so that we can have a working foreign key relationship
        # with registration_registrationprofile
        connection.cursor().execute("alter table auth_user ENGINE=InnoDB")

    def backwards(self, orm):
        connection.cursor().execute("alter table auth_user ENGINE=MyISAM")

    complete_apps = ['chart']
