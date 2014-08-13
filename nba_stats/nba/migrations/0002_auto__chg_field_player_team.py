# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Player.team'
        db.alter_column(u'nba_player', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, on_delete=models.SET_NULL, to=orm['nba.Team']))

    def backwards(self, orm):

        # Changing field 'Player.team'
        db.alter_column(u'nba_player', 'team_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['nba.Team']))

    models = {
        u'nba.game': {
            'Meta': {'object_name': 'Game'},
            'away': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_games'", 'to': u"orm['nba.Team']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_games'", 'to': u"orm['nba.Team']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nba.Player']", 'through': u"orm['nba.StatLine']", 'symmetrical': 'False'})
        },
        u'nba.nonplayer': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'NonPlayer'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'role': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        u'nba.official': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'Official'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        u'nba.player': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'Player'},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'height': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jersey': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pick': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True'}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nba.Position']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'null': 'True', 'on_delete': 'models.SET_NULL', 'to': u"orm['nba.Team']"}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3'})
        },
        u'nba.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        u'nba.statline': {
            'Meta': {'object_name': 'StatLine'},
            '_3pa': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            '_3pm': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'ast': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'blk': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'dreb': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'fga': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'fgm': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stats'", 'to': u"orm['nba.Game']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mins': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0', 'max_length': '2'}),
            'oreb': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'pf': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '1'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stats'", 'to': u"orm['nba.Player']"}),
            'stl': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'tov': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'})
        },
        u'nba.team': {
            'Meta': {'unique_together': "(('city', 'nickname'),)", 'object_name': 'Team'},
            'abbrev': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'arena': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'general_manager': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'gm_team'", 'unique': 'True', 'to': u"orm['nba.NonPlayer']"}),
            'head_coach': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'hc_team'", 'unique': 'True', 'to': u"orm['nba.NonPlayer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'owner': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'owner_team'", 'unique': 'True', 'to': u"orm['nba.NonPlayer']"}),
            'year_founded': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4'})
        }
    }

    complete_apps = ['nba']