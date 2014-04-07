# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Event.venue'
        db.delete_column(u'events_event', 'venue_id')

        # Adding M2M table for field venue on 'Event'
        m2m_table_name = db.shorten_name(u'events_event_venue')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'events.event'], null=False)),
            ('venue', models.ForeignKey(orm[u'events.venue'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'venue_id'])


    def backwards(self, orm):
        # Adding field 'Event.venue'
        db.add_column(u'events_event', 'venue',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='event_venue', null=True, to=orm['events.Venue'], blank=True),
                      keep_default=False)

        # Removing M2M table for field venue on 'Event'
        db.delete_table(db.shorten_name(u'events_event_venue'))


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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'clubs.club': {
            'Meta': {'object_name': 'Club'},
            'about': ('django.db.models.fields.CharField', [], {'max_length': '20000', 'blank': 'True'}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'convener': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'convener'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['userprofile.UserProfile']"}),
            'cover': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cover_club'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['litsoc.PhotoModel']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'image_club'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['litsoc.PhotoModel']"}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'clubs_links'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['litsoc.LinkModel']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'oneliner': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.event': {
            'Meta': {'object_name': 'Event'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'club': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'events'", 'null': 'True', 'to': u"orm['clubs.Club']"}),
            'coords': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'coord'", 'blank': 'True', 'to': u"orm['userprofile.UserProfile']"}),
            'cover': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cover_event'", 'null': 'True', 'to': u"orm['litsoc.PhotoModel']"}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'edited_by'", 'to': u"orm['userprofile.UserProfile']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '40000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'image_event'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['litsoc.PhotoModel']"}),
            'links': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'event_links'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['litsoc.LinkModel']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'oneliner': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'photo_coord': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'ph_coord'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['userprofile.UserProfile']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'venue': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'event_venue'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['events.Venue']"})
        },
        u'events.venue': {
            'Meta': {'object_name': 'Venue'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'litsoc.comment': {
            'Meta': {'object_name': 'Comment'},
            'anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'comment_by'", 'null': 'True', 'to': u"orm['userprofile.UserProfile']"}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '40000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'litsoc.linkmodel': {
            'Meta': {'object_name': 'LinkModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '300'})
        },
        u'litsoc.photomodel': {
            'Meta': {'object_name': 'PhotoModel'},
            'by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_by'", 'null': 'True', 'to': u"orm['userprofile.UserProfile']"}),
            'comments': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'photo_comments'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['litsoc.Comment']"}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '3000', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'userprofile.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'assigned': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'//avatar/default.jpg'", 'max_length': '100'}),
            'contact_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'hostel': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nick': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'typ': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['events']