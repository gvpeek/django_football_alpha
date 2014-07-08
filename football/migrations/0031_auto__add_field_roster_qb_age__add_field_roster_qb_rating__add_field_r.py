# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Roster.qb_age'
        db.add_column(u'football_roster', 'qb_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.qb_rating'
        db.add_column(u'football_roster', 'qb_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.rb_age'
        db.add_column(u'football_roster', 'rb_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.rb_rating'
        db.add_column(u'football_roster', 'rb_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.wr_age'
        db.add_column(u'football_roster', 'wr_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.wr_rating'
        db.add_column(u'football_roster', 'wr_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.og_age'
        db.add_column(u'football_roster', 'og_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.og_rating'
        db.add_column(u'football_roster', 'og_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.ot_age'
        db.add_column(u'football_roster', 'ot_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.ot_rating'
        db.add_column(u'football_roster', 'ot_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.c_age'
        db.add_column(u'football_roster', 'c_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.c_rating'
        db.add_column(u'football_roster', 'c_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.de_age'
        db.add_column(u'football_roster', 'de_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.de_rating'
        db.add_column(u'football_roster', 'de_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.dt_age'
        db.add_column(u'football_roster', 'dt_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.dt_rating'
        db.add_column(u'football_roster', 'dt_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.lb_age'
        db.add_column(u'football_roster', 'lb_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.lb_rating'
        db.add_column(u'football_roster', 'lb_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.cb_age'
        db.add_column(u'football_roster', 'cb_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.cb_rating'
        db.add_column(u'football_roster', 'cb_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.s_age'
        db.add_column(u'football_roster', 's_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.s_rating'
        db.add_column(u'football_roster', 's_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.p_age'
        db.add_column(u'football_roster', 'p_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.p_rating'
        db.add_column(u'football_roster', 'p_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.k_age'
        db.add_column(u'football_roster', 'k_age',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Roster.k_rating'
        db.add_column(u'football_roster', 'k_rating',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Roster.qb_age'
        db.delete_column(u'football_roster', 'qb_age')

        # Deleting field 'Roster.qb_rating'
        db.delete_column(u'football_roster', 'qb_rating')

        # Deleting field 'Roster.rb_age'
        db.delete_column(u'football_roster', 'rb_age')

        # Deleting field 'Roster.rb_rating'
        db.delete_column(u'football_roster', 'rb_rating')

        # Deleting field 'Roster.wr_age'
        db.delete_column(u'football_roster', 'wr_age')

        # Deleting field 'Roster.wr_rating'
        db.delete_column(u'football_roster', 'wr_rating')

        # Deleting field 'Roster.og_age'
        db.delete_column(u'football_roster', 'og_age')

        # Deleting field 'Roster.og_rating'
        db.delete_column(u'football_roster', 'og_rating')

        # Deleting field 'Roster.ot_age'
        db.delete_column(u'football_roster', 'ot_age')

        # Deleting field 'Roster.ot_rating'
        db.delete_column(u'football_roster', 'ot_rating')

        # Deleting field 'Roster.c_age'
        db.delete_column(u'football_roster', 'c_age')

        # Deleting field 'Roster.c_rating'
        db.delete_column(u'football_roster', 'c_rating')

        # Deleting field 'Roster.de_age'
        db.delete_column(u'football_roster', 'de_age')

        # Deleting field 'Roster.de_rating'
        db.delete_column(u'football_roster', 'de_rating')

        # Deleting field 'Roster.dt_age'
        db.delete_column(u'football_roster', 'dt_age')

        # Deleting field 'Roster.dt_rating'
        db.delete_column(u'football_roster', 'dt_rating')

        # Deleting field 'Roster.lb_age'
        db.delete_column(u'football_roster', 'lb_age')

        # Deleting field 'Roster.lb_rating'
        db.delete_column(u'football_roster', 'lb_rating')

        # Deleting field 'Roster.cb_age'
        db.delete_column(u'football_roster', 'cb_age')

        # Deleting field 'Roster.cb_rating'
        db.delete_column(u'football_roster', 'cb_rating')

        # Deleting field 'Roster.s_age'
        db.delete_column(u'football_roster', 's_age')

        # Deleting field 'Roster.s_rating'
        db.delete_column(u'football_roster', 's_rating')

        # Deleting field 'Roster.p_age'
        db.delete_column(u'football_roster', 'p_age')

        # Deleting field 'Roster.p_rating'
        db.delete_column(u'football_roster', 'p_rating')

        # Deleting field 'Roster.k_age'
        db.delete_column(u'football_roster', 'k_age')

        # Deleting field 'Roster.k_rating'
        db.delete_column(u'football_roster', 'k_rating')


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
        u'football.coach': {
            'Meta': {'object_name': 'Coach'},
            'fg_dist_probabilities': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'play_probabilities': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'skill': ('django.db.models.fields.IntegerField', [], {}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'coach_universe'", 'to': u"orm['football.Universe']"})
        },
        u'football.game': {
            'Meta': {'object_name': 'Game'},
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_away_team'", 'to': u"orm['football.Team']"}),
            'conference_game': ('django.db.models.fields.BooleanField', [], {}),
            'division_game': ('django.db.models.fields.BooleanField', [], {}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_home_team'", 'to': u"orm['football.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league_game': ('django.db.models.fields.BooleanField', [], {}),
            'number_of_overtime_periods': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'number_of_periods': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'playoff_game': ('django.db.models.fields.BooleanField', [], {}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_universe'", 'to': u"orm['football.Universe']"}),
            'use_overtime': ('django.db.models.fields.BooleanField', [], {}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_year'", 'to': u"orm['football.Year']"})
        },
        u'football.gamestats': {
            'Meta': {'object_name': 'GameStats'},
            'completion_pct': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'conv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'conv_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fg': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fg_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fumbles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gamestats_game'", 'to': u"orm['football.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intercepted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kick_return_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kick_returns': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kickoff_touchbacks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kickoff_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kickoffs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'outcome': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'pass_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pass_comp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pass_td': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pass_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_blocks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_return_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_returns': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_touchbacks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rush_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rush_td': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rush_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sacked': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'safeties': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_by_period': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'default': '[0, 0, 0, 0]', 'max_length': '30'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gamestats_team'", 'to': u"orm['football.Team']"}),
            'total_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gamestats_universe'", 'to': u"orm['football.Universe']"}),
            'xp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'xp_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'gamestats_year'", 'to': u"orm['football.Year']"})
        },
        u'football.league': {
            'Meta': {'object_name': 'League'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'pro'", 'max_length': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'league_universe'", 'to': u"orm['football.Universe']"})
        },
        u'football.leaguemembership': {
            'Meta': {'object_name': 'LeagueMembership'},
            'conference': ('django.db.models.fields.IntegerField', [], {}),
            'division': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'membership_league'", 'to': u"orm['football.League']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'membership_team'", 'to': u"orm['football.Team']"}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'membership_universe'", 'to': u"orm['football.Universe']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'membership_year'", 'to': u"orm['football.Year']"})
        },
        u'football.nickname': {
            'Meta': {'object_name': 'Nickname'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'pro': ('django.db.models.fields.BooleanField', [], {}),
            'semipro': ('django.db.models.fields.BooleanField', [], {})
        },
        u'football.playbook': {
            'Meta': {'object_name': 'Playbook'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'plays': ('django.db.models.fields.CharField', [], {'max_length': '10000'})
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
            'c': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'center'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'c_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'c_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'cornerback'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'cb_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cb_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'de': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'defensive end'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'de_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'de_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dt': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'defensive tackle'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'dt_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dt_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'k': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'kicker'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'k_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'k_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'linebacker'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'lb_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lb_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'og': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'offensive guard'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'og_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'og_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ot': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'offensive tackle'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'ot_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ot_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'p': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'punter'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'p_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'p_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'quarterback'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'qb_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'qb_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rb': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'running back'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'rb_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rb_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            's': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'safety'", 'null': 'True', 'to': u"orm['football.Player']"}),
            's_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            's_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roster_team'", 'to': u"orm['football.Team']"}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roster_universe'", 'to': u"orm['football.Universe']"}),
            'wr': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'wide receiver'", 'null': 'True', 'to': u"orm['football.Player']"}),
            'wr_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wr_rating': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'roster_year'", 'to': u"orm['football.Year']"})
        },
        u'football.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schedule_game'", 'to': u"orm['football.Game']"}),
            'game_number': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schedule_league'", 'to': u"orm['football.League']"}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schedule_universe'", 'to': u"orm['football.Universe']"}),
            'week': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schedule_year'", 'to': u"orm['football.Year']"})
        },
        u'football.team': {
            'Meta': {'object_name': 'Team'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.City']"}),
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_coach'", 'to': u"orm['football.Coach']"}),
            'draft_position_order': ('django.db.models.fields.CharField', [], {'default': '\'["K", "DT", "P", "QB", "OT", "CB", "OG", "LB", "DE", "WR", "S", "C", "RB"]\'', 'max_length': '200'}),
            'home_field_advantage': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'human_control': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.Nickname']"}),
            'playbook': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_playbook'", 'to': u"orm['football.Playbook']"}),
            'primary_color': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '30'}),
            'secondary_color': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '30'}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_universe'", 'to': u"orm['football.Universe']"})
        },
        u'football.teamstats': {
            'Meta': {'object_name': 'TeamStats'},
            'completion_pct': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'conv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'conv_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fg': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fg_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'fumbles': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intercepted': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kick_return_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kick_returns': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kickoff_touchbacks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kickoff_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'kickoffs': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'losses': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pass_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pass_comp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pass_td': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pass_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pct': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '4', 'decimal_places': '3'}),
            'punt_blocks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_return_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_returns': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_touchbacks': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punt_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'punts': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rush_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rush_td': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rush_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sacked': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'safeties': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_by_period': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'default': '[0, 0, 0, 0]', 'max_length': '30'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teamstats_team'", 'to': u"orm['football.Team']"}),
            'ties': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_yards': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teamstats_universe'", 'to': u"orm['football.Universe']"}),
            'wins': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'xp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'xp_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'teamstats_year'", 'to': u"orm['football.Year']"})
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