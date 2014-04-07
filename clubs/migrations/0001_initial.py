# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Club'
        db.create_table(u'clubs_club', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('oneliner', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('about', self.gf('django.db.models.fields.CharField')(max_length=20000, blank=True)),
            ('cover', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='cover_club', null=True, on_delete=models.SET_NULL, to=orm['litsoc.PhotoModel'])),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'clubs', ['Club'])

        # Adding M2M table for field convener on 'Club'
        m2m_table_name = db.shorten_name(u'clubs_club_convener')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('club', models.ForeignKey(orm[u'clubs.club'], null=False)),
            ('userprofile', models.ForeignKey(orm[u'userprofile.userprofile'], null=False))
        ))
        db.create_unique(m2m_table_name, ['club_id', 'userprofile_id'])

        # Adding M2M table for field images on 'Club'
        m2m_table_name = db.shorten_name(u'clubs_club_images')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('club', models.ForeignKey(orm[u'clubs.club'], null=False)),
            ('photomodel', models.ForeignKey(orm[u'litsoc.photomodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['club_id', 'photomodel_id'])

        # Adding M2M table for field links on 'Club'
        m2m_table_name = db.shorten_name(u'clubs_club_links')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('club', models.ForeignKey(orm[u'clubs.club'], null=False)),
            ('linkmodel', models.ForeignKey(orm[u'litsoc.linkmodel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['club_id', 'linkmodel_id'])

        # Adding model 'MusicClubRequest'
        db.create_table(u'clubs_musicclubrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('musiccardid', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('contact_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('rollno', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('slot', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'clubs', ['MusicClubRequest'])

        # Adding M2M table for field person on 'MusicClubRequest'
        m2m_table_name = db.shorten_name(u'clubs_musicclubrequest_person')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('musicclubrequest', models.ForeignKey(orm[u'clubs.musicclubrequest'], null=False)),
            ('musicclubperson', models.ForeignKey(orm[u'clubs.musicclubperson'], null=False))
        ))
        db.create_unique(m2m_table_name, ['musicclubrequest_id', 'musicclubperson_id'])

        # Adding model 'MusicClubPerson'
        db.create_table(u'clubs_musicclubperson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('rollno', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('is_leader', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'clubs', ['MusicClubPerson'])


    def backwards(self, orm):
        # Deleting model 'Club'
        db.delete_table(u'clubs_club')

        # Removing M2M table for field convener on 'Club'
        db.delete_table(db.shorten_name(u'clubs_club_convener'))

        # Removing M2M table for field images on 'Club'
        db.delete_table(db.shorten_name(u'clubs_club_images'))

        # Removing M2M table for field links on 'Club'
        db.delete_table(db.shorten_name(u'clubs_club_links'))

        # Deleting model 'MusicClubRequest'
        db.delete_table(u'clubs_musicclubrequest')

        # Removing M2M table for field person on 'MusicClubRequest'
        db.delete_table(db.shorten_name(u'clubs_musicclubrequest_person'))

        # Deleting model 'MusicClubPerson'
        db.delete_table(u'clubs_musicclubperson')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'oneliner': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'clubs.musicclubperson': {
            'Meta': {'object_name': 'MusicClubPerson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_leader': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'rollno': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'clubs.musicclubrequest': {
            'Meta': {'object_name': 'MusicClubRequest'},
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'contact_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'musiccardid': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'person': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'music_person'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['clubs.MusicClubPerson']"}),
            'rollno': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'slot': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
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

    complete_apps = ['clubs']