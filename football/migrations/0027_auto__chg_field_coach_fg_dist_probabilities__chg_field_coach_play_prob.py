# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Coach.fg_dist_probabilities'
        db.alter_column(u'football_coach', 'fg_dist_probabilities', self.gf('django.db.models.fields.CharField')(max_length=3000))

        # Changing field 'Coach.play_probabilities'
        db.alter_column(u'football_coach', 'play_probabilities', self.gf('django.db.models.fields.CharField')(max_length=3000))

    def backwards(self, orm):

        # Changing field 'Coach.fg_dist_probabilities'
        db.alter_column(u'football_coach', 'fg_dist_probabilities', self.gf('django.db.models.fields.CharField')(max_length=1000))

        # Changing field 'Coach.play_probabilities'
        db.alter_column(u'football_coach', 'play_probabilities', self.gf('django.db.models.fields.CharField')(max_length=2000))

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
            'fg_dist_probabilities': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'play_probabilities': ('django.db.models.fields.CharField', [], {'max_length': '3000'}),
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
            'draft_position_order': ('django.db.models.fields.CharField', [], {'default': '\'["C", "OG", "RB", "S", "QB", "LB", "WR", "P", "DT", "CB", "OT", "K", "DE"]\'', 'max_length': '200'}),
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