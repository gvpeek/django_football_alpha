# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stats'
        db.create_table(u'football_stats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('universe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teamstats_universe', to=orm['football.Universe'])),
            ('year', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teamstats_year', to=orm['football.Year'])),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='teamstats_team', to=orm['football.Team'])),
            ('wins', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('losses', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('ties', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pct', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=3)),
            ('score', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('opp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('diff', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('score_by_period', self.gf('django.db.models.fields.CommaSeparatedIntegerField')(default=[0, 0, 0, 0], max_length=30)),
            ('total_yards', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pass_att', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pass_comp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('completion_pct', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=3, decimal_places=2)),
            ('pass_yards', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('pass_td', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('intercepted', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('sacked', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rush_att', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rush_yards', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rush_td', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fumbles', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fg_att', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('fg', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('xp_att', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('xp', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('conv_att', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('conv', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('punts', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('punt_yards', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('punt_touchbacks', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('punt_blocks', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('punt_returns', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('punt_return_yards', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kickoffs', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kickoff_yards', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kickoff_touchbacks', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kick_returns', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('kick_return_yards', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('safeties', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'football', ['Stats'])

        # Deleting field 'PlayoffTeamStats.teamstats_ptr'
        db.delete_column(u'football_playoffteamstats', u'teamstats_ptr_id')

        # Adding field 'PlayoffTeamStats.stats_ptr'
        db.add_column(u'football_playoffteamstats', u'stats_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['football.Stats'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'TeamStats.punt_yards'
        db.delete_column(u'football_teamstats', 'punt_yards')

        # Deleting field 'TeamStats.kickoff_yards'
        db.delete_column(u'football_teamstats', 'kickoff_yards')

        # Deleting field 'TeamStats.fg'
        db.delete_column(u'football_teamstats', 'fg')

        # Deleting field 'TeamStats.pass_comp'
        db.delete_column(u'football_teamstats', 'pass_comp')

        # Deleting field 'TeamStats.punt_returns'
        db.delete_column(u'football_teamstats', 'punt_returns')

        # Deleting field 'TeamStats.diff'
        db.delete_column(u'football_teamstats', 'diff')

        # Deleting field 'TeamStats.xp'
        db.delete_column(u'football_teamstats', 'xp')

        # Deleting field 'TeamStats.pass_att'
        db.delete_column(u'football_teamstats', 'pass_att')

        # Deleting field 'TeamStats.rush_yards'
        db.delete_column(u'football_teamstats', 'rush_yards')

        # Deleting field 'TeamStats.kickoffs'
        db.delete_column(u'football_teamstats', 'kickoffs')

        # Deleting field 'TeamStats.sacked'
        db.delete_column(u'football_teamstats', 'sacked')

        # Deleting field 'TeamStats.fumbles'
        db.delete_column(u'football_teamstats', 'fumbles')

        # Deleting field 'TeamStats.pct'
        db.delete_column(u'football_teamstats', 'pct')

        # Deleting field 'TeamStats.kick_return_yards'
        db.delete_column(u'football_teamstats', 'kick_return_yards')

        # Deleting field 'TeamStats.opp'
        db.delete_column(u'football_teamstats', 'opp')

        # Deleting field 'TeamStats.total_yards'
        db.delete_column(u'football_teamstats', 'total_yards')

        # Deleting field 'TeamStats.punt_return_yards'
        db.delete_column(u'football_teamstats', 'punt_return_yards')

        # Deleting field 'TeamStats.kickoff_touchbacks'
        db.delete_column(u'football_teamstats', 'kickoff_touchbacks')

        # Deleting field 'TeamStats.conv_att'
        db.delete_column(u'football_teamstats', 'conv_att')

        # Deleting field 'TeamStats.punt_touchbacks'
        db.delete_column(u'football_teamstats', 'punt_touchbacks')

        # Deleting field 'TeamStats.intercepted'
        db.delete_column(u'football_teamstats', 'intercepted')

        # Deleting field 'TeamStats.pass_td'
        db.delete_column(u'football_teamstats', 'pass_td')

        # Deleting field 'TeamStats.completion_pct'
        db.delete_column(u'football_teamstats', 'completion_pct')

        # Deleting field 'TeamStats.universe'
        db.delete_column(u'football_teamstats', 'universe_id')

        # Deleting field 'TeamStats.xp_att'
        db.delete_column(u'football_teamstats', 'xp_att')

        # Deleting field 'TeamStats.conv'
        db.delete_column(u'football_teamstats', 'conv')

        # Deleting field 'TeamStats.year'
        db.delete_column(u'football_teamstats', 'year_id')

        # Deleting field 'TeamStats.id'
        db.delete_column(u'football_teamstats', u'id')

        # Deleting field 'TeamStats.rush_att'
        db.delete_column(u'football_teamstats', 'rush_att')

        # Deleting field 'TeamStats.safeties'
        db.delete_column(u'football_teamstats', 'safeties')

        # Deleting field 'TeamStats.score'
        db.delete_column(u'football_teamstats', 'score')

        # Deleting field 'TeamStats.score_by_period'
        db.delete_column(u'football_teamstats', 'score_by_period')

        # Deleting field 'TeamStats.team'
        db.delete_column(u'football_teamstats', 'team_id')

        # Deleting field 'TeamStats.punts'
        db.delete_column(u'football_teamstats', 'punts')

        # Deleting field 'TeamStats.fg_att'
        db.delete_column(u'football_teamstats', 'fg_att')

        # Deleting field 'TeamStats.ties'
        db.delete_column(u'football_teamstats', 'ties')

        # Deleting field 'TeamStats.rush_td'
        db.delete_column(u'football_teamstats', 'rush_td')

        # Deleting field 'TeamStats.wins'
        db.delete_column(u'football_teamstats', 'wins')

        # Deleting field 'TeamStats.losses'
        db.delete_column(u'football_teamstats', 'losses')

        # Deleting field 'TeamStats.kick_returns'
        db.delete_column(u'football_teamstats', 'kick_returns')

        # Deleting field 'TeamStats.pass_yards'
        db.delete_column(u'football_teamstats', 'pass_yards')

        # Deleting field 'TeamStats.punt_blocks'
        db.delete_column(u'football_teamstats', 'punt_blocks')

        # Adding field 'TeamStats.stats_ptr'
        db.add_column(u'football_teamstats', u'stats_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['football.Stats'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Stats'
        db.delete_table(u'football_stats')

        # Adding field 'PlayoffTeamStats.teamstats_ptr'
        db.add_column(u'football_playoffteamstats', u'teamstats_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['football.TeamStats'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'PlayoffTeamStats.stats_ptr'
        db.delete_column(u'football_playoffteamstats', u'stats_ptr_id')

        # Adding field 'TeamStats.punt_yards'
        db.add_column(u'football_teamstats', 'punt_yards',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.kickoff_yards'
        db.add_column(u'football_teamstats', 'kickoff_yards',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.fg'
        db.add_column(u'football_teamstats', 'fg',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.pass_comp'
        db.add_column(u'football_teamstats', 'pass_comp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.punt_returns'
        db.add_column(u'football_teamstats', 'punt_returns',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.diff'
        db.add_column(u'football_teamstats', 'diff',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.xp'
        db.add_column(u'football_teamstats', 'xp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.pass_att'
        db.add_column(u'football_teamstats', 'pass_att',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.rush_yards'
        db.add_column(u'football_teamstats', 'rush_yards',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.kickoffs'
        db.add_column(u'football_teamstats', 'kickoffs',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.sacked'
        db.add_column(u'football_teamstats', 'sacked',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.fumbles'
        db.add_column(u'football_teamstats', 'fumbles',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.pct'
        db.add_column(u'football_teamstats', 'pct',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=4, decimal_places=3),
                      keep_default=False)

        # Adding field 'TeamStats.kick_return_yards'
        db.add_column(u'football_teamstats', 'kick_return_yards',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.opp'
        db.add_column(u'football_teamstats', 'opp',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.total_yards'
        db.add_column(u'football_teamstats', 'total_yards',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.punt_return_yards'
        db.add_column(u'football_teamstats', 'punt_return_yards',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.kickoff_touchbacks'
        db.add_column(u'football_teamstats', 'kickoff_touchbacks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.conv_att'
        db.add_column(u'football_teamstats', 'conv_att',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.punt_touchbacks'
        db.add_column(u'football_teamstats', 'punt_touchbacks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.intercepted'
        db.add_column(u'football_teamstats', 'intercepted',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.pass_td'
        db.add_column(u'football_teamstats', 'pass_td',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.completion_pct'
        db.add_column(u'football_teamstats', 'completion_pct',
                      self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'TeamStats.universe'
        db.add_column(u'football_teamstats', 'universe',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='teamstats_universe', to=orm['football.Universe']),
                      keep_default=False)

        # Adding field 'TeamStats.xp_att'
        db.add_column(u'football_teamstats', 'xp_att',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.conv'
        db.add_column(u'football_teamstats', 'conv',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.year'
        db.add_column(u'football_teamstats', 'year',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='teamstats_year', to=orm['football.Year']),
                      keep_default=False)

        # Adding field 'TeamStats.id'
        db.add_column(u'football_teamstats', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True),
                      keep_default=False)

        # Adding field 'TeamStats.rush_att'
        db.add_column(u'football_teamstats', 'rush_att',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.safeties'
        db.add_column(u'football_teamstats', 'safeties',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.score'
        db.add_column(u'football_teamstats', 'score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.score_by_period'
        db.add_column(u'football_teamstats', 'score_by_period',
                      self.gf('django.db.models.fields.CommaSeparatedIntegerField')(default=[0, 0, 0, 0], max_length=30),
                      keep_default=False)

        # Adding field 'TeamStats.team'
        db.add_column(u'football_teamstats', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=0, related_name='teamstats_team', to=orm['football.Team']),
                      keep_default=False)

        # Adding field 'TeamStats.punts'
        db.add_column(u'football_teamstats', 'punts',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.fg_att'
        db.add_column(u'football_teamstats', 'fg_att',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.ties'
        db.add_column(u'football_teamstats', 'ties',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.rush_td'
        db.add_column(u'football_teamstats', 'rush_td',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.wins'
        db.add_column(u'football_teamstats', 'wins',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.losses'
        db.add_column(u'football_teamstats', 'losses',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.kick_returns'
        db.add_column(u'football_teamstats', 'kick_returns',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.pass_yards'
        db.add_column(u'football_teamstats', 'pass_yards',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'TeamStats.punt_blocks'
        db.add_column(u'football_teamstats', 'punt_blocks',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'TeamStats.stats_ptr'
        db.delete_column(u'football_teamstats', u'stats_ptr_id')


    models = {
        u'football.champions': {
            'Meta': {'object_name': 'Champions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'champions_league'", 'to': u"orm['football.League']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'champions_team'", 'to': u"orm['football.Team']"}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'champions_universe'", 'to': u"orm['football.Universe']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'champions_year'", 'to': u"orm['football.Year']"})
        },
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
            'conference_game': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'division_game': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'game_home_team'", 'to': u"orm['football.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league_game': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'number_of_overtime_periods': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'number_of_periods': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'playoff_game': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'number_playoff_teams': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
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
        u'football.playoffteams': {
            'Meta': {'object_name': 'PlayoffTeams'},
            'eliminated': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'league': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'playoff_league'", 'to': u"orm['football.League']"}),
            'qualification': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'seed': ('django.db.models.fields.IntegerField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'playoff_team'", 'to': u"orm['football.Team']"}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'playoff_universe'", 'to': u"orm['football.Universe']"}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'playoff_year'", 'to': u"orm['football.Year']"})
        },
        u'football.playoffteamstats': {
            'Meta': {'object_name': 'PlayoffTeamStats', '_ormbases': [u'football.Stats']},
            u'stats_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['football.Stats']", 'unique': 'True', 'primary_key': 'True'})
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
            'played': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'universe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schedule_universe'", 'to': u"orm['football.Universe']"}),
            'week': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'schedule_year'", 'to': u"orm['football.Year']"})
        },
        u'football.stats': {
            'Meta': {'object_name': 'Stats'},
            'completion_pct': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '3', 'decimal_places': '2'}),
            'conv': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'conv_att': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'diff': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
            'opp': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
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
        u'football.team': {
            'Meta': {'object_name': 'Team'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['football.City']"}),
            'coach': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'team_coach'", 'to': u"orm['football.Coach']"}),
            'draft_position_order': ('django.db.models.fields.CharField', [], {'default': '\'["CB", "S", "C", "LB", "WR", "RB", "K", "OG", "OT", "QB", "DE", "P", "DT"]\'', 'max_length': '200'}),
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
            'Meta': {'object_name': 'TeamStats', '_ormbases': [u'football.Stats']},
            u'stats_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['football.Stats']", 'unique': 'True', 'primary_key': 'True'})
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