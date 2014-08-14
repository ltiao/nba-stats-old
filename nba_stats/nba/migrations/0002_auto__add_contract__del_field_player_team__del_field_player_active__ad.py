# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contract'
        db.create_table(u'nba_contract', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contracts', to=orm['nba.Team'])),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(related_name='contracts', to=orm['nba.Player'])),
            ('season_start', self.gf('django.db.models.fields.DateField')()),
            ('season_end', self.gf('django.db.models.fields.DateField')(null=True)),
            ('is_in_force', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'nba', ['Contract'])

        # Deleting field 'Player.team'
        db.delete_column(u'nba_player', 'team_id')

        # Deleting field 'Player.active'
        db.delete_column(u'nba_player', 'active')

        # Adding field 'Player.nba_player_id'
        db.add_column(u'nba_player', 'nba_player_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, unique=True),
                      keep_default=False)

        # Adding field 'Player.nba_player_code'
        db.add_column(u'nba_player', 'nba_player_code',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=30),
                      keep_default=False)

        # Adding field 'Player.is_active'
        db.add_column(u'nba_player', 'is_active',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Player.weight'
        db.alter_column(u'nba_player', 'weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3, null=True))

        # Changing field 'Player.country'
        db.alter_column(u'nba_player', 'country', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Player.height'
        db.alter_column(u'nba_player', 'height', self.gf('django.db.models.fields.CharField')(max_length=20))

        # Renaming column for 'Player.position' to match new field type.
        db.rename_column(u'nba_player', 'position_id', 'position')
        # Changing field 'Player.position'
        db.alter_column(u'nba_player', 'position', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Removing index on 'Player', fields ['position']
        db.delete_index(u'nba_player', ['position_id'])


        # Changing field 'Player.jersey'
        db.alter_column(u'nba_player', 'jersey', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True))

        # Changing field 'Official.country'
        db.alter_column(u'nba_official', 'country', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'NonPlayer.country'
        db.alter_column(u'nba_nonplayer', 'country', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))
        # Deleting field 'Team.year_founded'
        db.delete_column(u'nba_team', 'year_founded')

        # Adding field 'Team.founded'
        db.add_column(u'nba_team', 'founded',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=2014, max_length=4),
                      keep_default=False)


    def backwards(self, orm):
        # Adding index on 'Player', fields ['position']
        db.create_index(u'nba_player', ['position_id'])

        # Deleting model 'Contract'
        db.delete_table(u'nba_contract')


        # User chose to not deal with backwards NULL issues for 'Player.team'
        raise RuntimeError("Cannot reverse this migration. 'Player.team' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Player.team'
        db.add_column(u'nba_player', 'team',
                      self.gf('django.db.models.fields.related.ForeignKey')(related_name='players', to=orm['nba.Team']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Player.active'
        raise RuntimeError("Cannot reverse this migration. 'Player.active' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Player.active'
        db.add_column(u'nba_player', 'active',
                      self.gf('django.db.models.fields.BooleanField')(),
                      keep_default=False)

        # Deleting field 'Player.nba_player_id'
        db.delete_column(u'nba_player', 'nba_player_id')

        # Deleting field 'Player.nba_player_code'
        db.delete_column(u'nba_player', 'nba_player_code')

        # Deleting field 'Player.is_active'
        db.delete_column(u'nba_player', 'is_active')


        # User chose to not deal with backwards NULL issues for 'Player.weight'
        raise RuntimeError("Cannot reverse this migration. 'Player.weight' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Player.weight'
        db.alter_column(u'nba_player', 'weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3))

        # Changing field 'Player.country'
        db.alter_column(u'nba_player', 'country', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Player.height'
        db.alter_column(u'nba_player', 'height', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2))

        # Renaming column for 'Player.position' to match new field type.
        db.rename_column(u'nba_player', 'position', 'position_id')
        # Changing field 'Player.position'
        db.alter_column(u'nba_player', 'position_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nba.Position']))

        # User chose to not deal with backwards NULL issues for 'Player.jersey'
        raise RuntimeError("Cannot reverse this migration. 'Player.jersey' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Player.jersey'
        db.alter_column(u'nba_player', 'jersey', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2))

        # Changing field 'Official.country'
        db.alter_column(u'nba_official', 'country', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'NonPlayer.country'
        db.alter_column(u'nba_nonplayer', 'country', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # User chose to not deal with backwards NULL issues for 'Team.year_founded'
        raise RuntimeError("Cannot reverse this migration. 'Team.year_founded' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Team.year_founded'
        db.add_column(u'nba_team', 'year_founded',
                      self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4),
                      keep_default=False)

        # Deleting field 'Team.founded'
        db.delete_column(u'nba_team', 'founded')


    models = {
        u'nba.contract': {
            'Meta': {'object_name': 'Contract'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_in_force': ('django.db.models.fields.BooleanField', [], {}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contracts'", 'to': u"orm['nba.Player']"}),
            'season_end': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'season_start': ('django.db.models.fields.DateField', [], {}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contracts'", 'to': u"orm['nba.Team']"})
        },
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
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'role': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        u'nba.official': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'Official'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'})
        },
        u'nba.player': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'Player'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {}),
            'jersey': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'nba_player_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'nba_player_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'pick': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True'})
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
            'founded': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4'}),
            'general_manager': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'gm_team'", 'unique': 'True', 'to': u"orm['nba.NonPlayer']"}),
            'head_coach': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'hc_team'", 'unique': 'True', 'to': u"orm['nba.NonPlayer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'owner': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'owner_team'", 'unique': 'True', 'to': u"orm['nba.NonPlayer']"}),
            'players': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nba.Player']", 'through': u"orm['nba.Contract']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['nba']