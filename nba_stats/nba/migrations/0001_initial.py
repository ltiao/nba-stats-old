# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'nba_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='players', to=orm['nba.Team'])),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('jersey', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2)),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nba.Position'])),
            ('height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3)),
            ('pick', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True)),
        ))
        db.send_create_signal(u'nba', ['Player'])

        # Adding model 'NonPlayer'
        db.create_table(u'nba_nonplayer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
            ('role', self.gf('django.db.models.fields.IntegerField')(max_length=1)),
        ))
        db.send_create_signal(u'nba', ['NonPlayer'])

        # Adding model 'Official'
        db.create_table(u'nba_official', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2, null=True)),
        ))
        db.send_create_signal(u'nba', ['Official'])

        # Adding model 'Team'
        db.create_table(u'nba_team', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('abbrev', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('nickname', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('arena', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('year_founded', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4)),
            ('general_manager', self.gf('django.db.models.fields.related.OneToOneField')(related_name='gm_team', unique=True, to=orm['nba.NonPlayer'])),
            ('head_coach', self.gf('django.db.models.fields.related.OneToOneField')(related_name='hc_team', unique=True, to=orm['nba.NonPlayer'])),
            ('owner', self.gf('django.db.models.fields.related.OneToOneField')(related_name='owner_team', unique=True, to=orm['nba.NonPlayer'])),
        ))
        db.send_create_signal(u'nba', ['Team'])

        # Adding unique constraint on 'Team', fields ['city', 'nickname']
        db.create_unique(u'nba_team', ['city', 'nickname'])

        # Adding model 'StatLine'
        db.create_table(u'nba_statline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stats', to=orm['nba.Player'])),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stats', to=orm['nba.Game'])),
            ('mins', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0, max_length=2)),
            ('fgm', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('fga', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('_3pm', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('_3pa', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('oreb', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('dreb', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('ast', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('stl', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('blk', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('tov', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('pf', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=1)),
        ))
        db.send_create_signal(u'nba', ['StatLine'])

        # Adding model 'Game'
        db.create_table(u'nba_game', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('home', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_games', to=orm['nba.Team'])),
            ('away', self.gf('django.db.models.fields.related.ForeignKey')(related_name='away_games', to=orm['nba.Team'])),
        ))
        db.send_create_signal(u'nba', ['Game'])

        # Adding model 'Position'
        db.create_table(u'nba_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
        ))
        db.send_create_signal(u'nba', ['Position'])


    def backwards(self, orm):
        # Removing unique constraint on 'Team', fields ['city', 'nickname']
        db.delete_unique(u'nba_team', ['city', 'nickname'])

        # Deleting model 'Player'
        db.delete_table(u'nba_player')

        # Deleting model 'NonPlayer'
        db.delete_table(u'nba_nonplayer')

        # Deleting model 'Official'
        db.delete_table(u'nba_official')

        # Deleting model 'Team'
        db.delete_table(u'nba_team')

        # Deleting model 'StatLine'
        db.delete_table(u'nba_statline')

        # Deleting model 'Game'
        db.delete_table(u'nba_game')

        # Deleting model 'Position'
        db.delete_table(u'nba_position')


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
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'players'", 'to': u"orm['nba.Team']"}),
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