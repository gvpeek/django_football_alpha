# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Roster.rb'
        db.add_column(u'football_roster', 'rb',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='running back', to=orm['football.Player']),
                      keep_default=False)

        # Adding field 'Roster.wr'
        db.add_column(u'football_roster', 'wr',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='wide receiver', to=orm['football.Player']),
                      keep_default=False)

        # Adding field 'Roster.ol'
        db.add_column(u'football_roster', 'ol',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='offensive line', to=orm['football.Player']),
                      keep_default=False)

        # Adding field 'Roster.dl'
        db.add_column(u'football_roster', 'dl',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='defensive line', to=orm['football.Player']),
                      keep_default=False)

        # Adding field 'Roster.lb'
        db.add_column(u'football_roster', 'lb',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='linebacker', to=orm['football.Player']),
                      keep_default=False)

        # Adding field 'Roster.cb'
        db.add_column(u'football_roster', 'cb',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='cornerback', to=orm['football.Player']),
                      keep_default=False)

        # Adding field 'Roster.s'
        db.add_column(u'football_roster', 's',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='safety', to=orm['football.Player']),
                      keep_default=False)

        # Adding field 'Roster.p'
        db.add_column(u'football_roster', 'p',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='punter', to=orm['football.Player']),
                      keep_default=False)

        # Adding field 'Roster.k'
        db.add_column(u'football_roster', 'k',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='kicker', to=orm['football.Player']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Roster.rb'
        db.delete_column(u'football_roster', 'rb_id')

        # Deleting field 'Roster.wr'
        db.delete_column(u'football_roster', 'wr_id')

        # Deleting field 'Roster.ol'
        db.delete_column(u'football_roster', 'ol_id')

        # Deleting field 'Roster.dl'
        db.delete_column(u'football_roster', 'dl_id')

        # Deleting field 'Roster.lb'
        db.delete_column(u'football_roster', 'lb_id')

        # Deleting field 'Roster.cb'
        db.delete_column(u'football_roster', 'cb_id')

        # Deleting field 'Roster.s'
        db.delete_column(u'football_roster', 's_id')

        # Deleting field 'Roster.p'
        db.delete_column(u'football_roster', 'p_id')

        # Deleting field 'Roster.k'
        db.delete_column(u'football_roster', 'k_id')


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
        u'football.roster': {
            'Meta': {'object_name': 'Roster'},
            'cb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cornerback'", 'to': u"orm['football.Player']"}),
            'dl': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'defensive line'", 'to': u"orm['football.Player']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'k': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'kicker'", 'to': u"orm['football.Player']"}),
            'lb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'linebacker'", 'to': u"orm['football.Player']"}),
            'ol': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'offensive line'", 'to': u"orm['football.Player']"}),
            'p': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'punter'", 'to': u"orm['football.Player']"}),
            'qb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'quarterback'", 'to': u"orm['football.Player']"}),
            'rb': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'running back'", 'to': u"orm['football.Player']"}),
            's': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'safety'", 'to': u"orm['football.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.Team']"}),
            'wr': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'wide receiver'", 'to': u"orm['football.Player']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.Year']"})
        },
        u'football.team': {
            'Meta': {'object_name': 'Team'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.City']"}),
            'home_field_advantage': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'human_control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.Nickname']"})
        },
        u'football.year': {
            'Meta': {'object_name': 'Year'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '1960'})
        }
    }

    complete_apps = ['football']