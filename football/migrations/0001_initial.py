# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Year'
        db.create_table(u'football_year', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')(default=1960)),
        ))
        db.send_create_signal(u'football', ['Year'])

        # Adding model 'Player'
        db.create_table(u'football_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('age', self.gf('django.db.models.fields.IntegerField')(default=11)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('constitution', self.gf('django.db.models.fields.IntegerField')()),
            ('retired', self.gf('django.db.models.fields.BooleanField')()),
            ('apex_age', self.gf('django.db.models.fields.IntegerField')()),
            ('growth_rate', self.gf('django.db.models.fields.IntegerField')()),
            ('declination_rate', self.gf('django.db.models.fields.IntegerField')()),
            ('ratings', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'football', ['Player'])

        # Adding model 'City'
        db.create_table(u'football_city', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('pro', self.gf('django.db.models.fields.BooleanField')()),
            ('semipro', self.gf('django.db.models.fields.BooleanField')()),
            ('amateur', self.gf('django.db.models.fields.BooleanField')()),
            ('region', self.gf('django.db.models.fields.IntegerField')()),
            ('division', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'football', ['City'])

        # Adding model 'Nickname'
        db.create_table(u'football_nickname', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('pro', self.gf('django.db.models.fields.BooleanField')()),
            ('semipro', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'football', ['Nickname'])

        # Adding model 'Team'
        db.create_table(u'football_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['football.City'])),
            ('human_control', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('home_field_advantage', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'football', ['Team'])


    def backwards(self, orm):
        # Deleting model 'Year'
        db.delete_table(u'football_year')

        # Deleting model 'Player'
        db.delete_table(u'football_player')

        # Deleting model 'City'
        db.delete_table(u'football_city')

        # Deleting model 'Nickname'
        db.delete_table(u'football_nickname')

        # Deleting model 'Team'
        db.delete_table(u'football_team')


    models = {
        u'football.city': {
            'Meta': {'object_name': 'City'},
            'amateur': ('django.db.models.fields.BooleanField', [], {}),
            'division': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pro': ('django.db.models.fields.BooleanField', [], {}),
            'region': ('django.db.models.fields.IntegerField', [], {}),
            'semipro': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        u'football.nickname': {
            'Meta': {'object_name': 'Nickname'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pro': ('django.db.models.fields.BooleanField', [], {}),
            'semipro': ('django.db.models.fields.BooleanField', [], {})
        },
        u'football.player': {
            'Meta': {'object_name': 'Player'},
            'age': ('django.db.models.fields.IntegerField', [], {'default': '11'}),
            'apex_age': ('django.db.models.fields.IntegerField', [], {}),
            'constitution': ('django.db.models.fields.IntegerField', [], {}),
            'declination_rate': ('django.db.models.fields.IntegerField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'growth_rate': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'ratings': ('django.db.models.fields.IntegerField', [], {}),
            'retired': ('django.db.models.fields.BooleanField', [], {})
        },
        u'football.team': {
            'Meta': {'object_name': 'Team'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.City']"}),
            'home_field_advantage': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'human_control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'football.year': {
            'Meta': {'object_name': 'Year'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '1960'})
        }
    }

    complete_apps = ['football']