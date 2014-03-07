# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artwork'
        db.create_table(u'jukebox_core_artwork', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('MD5', self.gf('django.db.models.fields.CharField')(unique=True, max_length=32)),
            ('Image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True)),
            ('Image_height', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
            ('Image_width', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'jukebox_core', ['Artwork'])

        # Adding field 'Song.Artwork'
        db.add_column(u'jukebox_core_song', 'Artwork',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['jukebox_core.Artwork'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Artwork'
        db.delete_table(u'jukebox_core_artwork')

        # Deleting field 'Song.Artwork'
        db.delete_column(u'jukebox_core_song', 'Artwork_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'jukebox_core.album': {
            'Meta': {'ordering': "['Title']", 'object_name': 'Album'},
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jukebox_core.artist': {
            'Meta': {'ordering': "['Name']", 'object_name': 'Artist'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jukebox_core.artwork': {
            'Image': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'Image_height': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'Image_width': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'MD5': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'Meta': {'object_name': 'Artwork'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jukebox_core.favourite': {
            'Created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-Created']", 'unique_together': "(('Song', 'User'),)", 'object_name': 'Favourite'},
            'Song': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jukebox_core.Song']"}),
            'User': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jukebox_core.genre': {
            'Meta': {'ordering': "['Name']", 'object_name': 'Genre'},
            'Name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jukebox_core.history': {
            'Created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Meta': {'ordering': "['-Created']", 'object_name': 'History'},
            'Song': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jukebox_core.Song']"}),
            'User': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'null': 'True', 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jukebox_core.player': {
            'Meta': {'object_name': 'Player'},
            'Pid': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jukebox_core.queue': {
            'Created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'Meta': {'object_name': 'Queue'},
            'Song': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jukebox_core.Song']", 'unique': 'True'}),
            'User': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'jukebox_core.song': {
            'Album': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jukebox_core.Album']", 'null': 'True'}),
            'Artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jukebox_core.Artist']"}),
            'Artwork': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jukebox_core.Artwork']", 'null': 'True', 'blank': 'True'}),
            'Filename': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'Genre': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['jukebox_core.Genre']", 'null': 'True'}),
            'Length': ('django.db.models.fields.IntegerField', [], {}),
            'Meta': {'ordering': "['Title', 'Artist', 'Album']", 'object_name': 'Song'},
            'Title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'Year': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['jukebox_core']