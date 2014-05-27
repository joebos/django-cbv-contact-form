# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Department'
        db.create_table('contact_form_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['sites.Site'], blank=True)),
        ))
        db.send_create_signal('contact_form', ['Department'])

        # Adding model 'Subject'
        db.create_table('contact_form_subject', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact_form.Department'])),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['sites.Site'], blank=True)),
        ))
        db.send_create_signal('contact_form', ['Subject'])

        # Adding model 'Message'
        db.create_table('contact_form_message', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sender_name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('sender_email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contact_form.Subject'])),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=4096)),
            ('ip', self.gf('django.db.models.fields.IPAddressField')(null=True, max_length=15, blank=True)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['sites.Site'], blank=True)),
        ))
        db.send_create_signal('contact_form', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Department'
        db.delete_table('contact_form_department')

        # Deleting model 'Subject'
        db.delete_table('contact_form_subject')

        # Deleting model 'Message'
        db.delete_table('contact_form_message')


    models = {
        'contact_form.department': {
            'Meta': {'object_name': 'Department'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['sites.Site']", 'blank': 'True'})
        },
        'contact_form.message': {
            'Meta': {'object_name': 'Message'},
            'date_created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.IPAddressField', [], {'null': 'True', 'max_length': '15', 'blank': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '4096'}),
            'sender_email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'sender_name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['sites.Site']", 'blank': 'True'}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact_form.Subject']"})
        },
        'contact_form.subject': {
            'Meta': {'object_name': 'Subject'},
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contact_form.Department']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['sites.Site']", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        'sites.site': {
            'Meta': {'db_table': "'django_site'", 'object_name': 'Site', 'ordering': "('domain',)"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['contact_form']