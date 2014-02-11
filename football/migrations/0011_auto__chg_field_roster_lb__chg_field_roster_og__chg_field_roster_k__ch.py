# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Roster.lb'
        db.alter_column(u'football_roster', 'lb_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.og'
        db.alter_column(u'football_roster', 'og_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.k'
        db.alter_column(u'football_roster', 'k_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.de'
        db.alter_column(u'football_roster', 'de_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.p'
        db.alter_column(u'football_roster', 'p_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.s'
        db.alter_column(u'football_roster', 's_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.qb'
        db.alter_column(u'football_roster', 'qb_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.wr'
        db.alter_column(u'football_roster', 'wr_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.rb'
        db.alter_column(u'football_roster', 'rb_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.dt'
        db.alter_column(u'football_roster', 'dt_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.ot'
        db.alter_column(u'football_roster', 'ot_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

        # Changing field 'Roster.cb'
        db.alter_column(u'football_roster', 'cb_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['football.Player']))

    def backwards(self, orm):

        # Changing field 'Roster.lb'
        db.alter_column(u'football_roster', 'lb_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.og'
        db.alter_column(u'football_roster', 'og_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.k'
        db.alter_column(u'football_roster', 'k_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.de'
        db.alter_column(u'football_roster', 'de_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.p'
        db.alter_column(u'football_roster', 'p_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.s'
        db.alter_column(u'football_roster', 's_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.qb'
        db.alter_column(u'football_roster', 'qb_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.wr'
        db.alter_column(u'football_roster', 'wr_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.rb'
        db.alter_column(u'football_roster', 'rb_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.dt'
        db.alter_column(u'football_roster', 'dt_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.ot'
        db.alter_column(u'football_roster', 'ot_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

        # Changing field 'Roster.cb'
        db.alter_column(u'football_roster', 'cb_id', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['football.Player']))

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
            'retired': ('django.db.models.fields.BooleanField', [], {}),
            'signed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'player_universe'", 'to': u"orm['football.Universe']"})
        },
        u'football.roster': {
            'Meta': {'object_name': 'Roster'},
            'cb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cornerback'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'de': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'defensive end'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'dt': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'defensive tackle'", 'null': 'True', 'to': u"orm['football.Player']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'k': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'kicker'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'lb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'linebacker'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'og': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'offensive guard'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'ot': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'offensive tackle'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'p': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'punter'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'qb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'quarterback'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'rb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'running back'", 'null': 'True', 'to': u"orm['football.Player']"}),
            's': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'safety'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roster_team'", 'to': u"orm['football.Team']"}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roster_universe'", 'to': u"orm['football.Universe']"}),
            'wr': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'wide receiver'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roster_year'", 'to': u"orm['football.Year']"})
        },
        u'football.team': {
            'Meta': {'object_name': 'Team'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.City']"}),
            'home_field_advantage': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'human_control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.Nickname']"}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_universe'", 'to': u"orm['football.Universe']"})
        },
        u'football.universe': {
            'Meta': {'object_name': 'Universe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'football.year': {
            'Meta': {'unique_together': "(('year', 'universe'),)", 'object_name': 'Year'},
            'current_year': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'year_universe'", 'to': u"orm['football.Universe']"}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '1960'})
        }
    }

    complete_apps = ['football']