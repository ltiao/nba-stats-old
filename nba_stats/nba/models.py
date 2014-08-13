from django.db import models
from datetime import date, datetime

# TODO: For our app, it makes sense to
# use our own primary keys that are implicitly
# handled by Django since we don't want our
# APIs and whatnot to make it blatantly obvious
# that we've taken the data from stats.nba.com
# That said, we still need to keep track of the
# proprietry stats.nba.com IDs of each respective 
# object type (Player, Team, Game, etc.) so that 
# we are able to generate links dynamically to NBA.com
# or je ne sais quoi. To accomplish this, we could 
# define a abstract base NBAStatsObject class which contains
# a unique integer field and have all relevant models
# subclass this.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthdate = models.DateField()
    school = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True) # might use django-country for this field

    @property
    def full_name(self):
        return u'{fname} {lname}'.format(fname=self.first_name, lname=self.last_name)

    @property
    def age(self):
        today = date.today()
        return today.year - self.birthdate.year - ((today.month, today.day) \
            < (self.birthdate.month, self.birthdate.day))

    def __unicode__(self):
        return self.full_name

    class Meta:
        abstract = True
        ordering = ['first_name', 'last_name']

class Player(Person):
    is_active = models.BooleanField()
    # May need to revisit this since '00' (not '0') might be allowed
    jersey = models.PositiveSmallIntegerField(
        verbose_name = 'Jersey number',
        max_length = 2,
        null = True,
    )
    # I've created Position as a separate model
    # since this could be a ManyToMany relation
    # (I've seen many players listed as 'SG-SF', 'PF-C', etc.)
    position = models.ForeignKey('Position', null=True)
    height = models.PositiveSmallIntegerField(
        verbose_name = 'Height (in)', 
        max_length = 2,
        null = True,
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name = 'Weight (lb)', 
        max_length = 3,
        null = True,
    )
    pick = models.PositiveSmallIntegerField(
        verbose_name = 'Draft Pick', 
        max_length = 2,
        null = True # Used to signify 'Undrafted'
    )

    @property
    def round(self):
        # return 1 if self.pick < 31 else 2
        return int(self.pick/31) + 1   

    # TODO: Integrate some python unit conversion
    # library to support simple conversions
    # to/from metric system, etc.

    def __unicode__(self):
        return u'#{nbr} - '.format(nbr=self.jersey) + super(Player, self).__unicode__()

class NonPlayer(Person):
    # TODO: Probably use a ForeignKey relation
    # or even ManyToMany here like as has been 
    # done for Player positions
    # (e.g. Popovich is Head Coach and some other
    # role, I forgot, PoBO?)
    role = models.IntegerField(max_length=1)

# TODO: (or maybe not)
class Official(Person):
    pass

class Team(models.Model):
    abbrev = models.CharField(
        verbose_name = 'Abbreviation',
        max_length = 3, 
        unique = True
    )
    city = models.CharField(max_length=16)
    nickname = models.CharField(max_length=30, unique=True)
    
    arena = models.CharField(max_length=32)
    founded = models.PositiveSmallIntegerField(
        verbose_name = 'Year Founded', 
        max_length = 4
    )

    players = models.ManyToManyField('Player', through='Contract')

    # Could also have NonPlayers with roles such as GM, Owner, 
    # Head Coach, etc. and ForeignKey Team affiliations
    # (though it is true that this would not enforce a OneToOne constraint)
    general_manager = models.OneToOneField('NonPlayer', related_name='gm_team')
    head_coach = models.OneToOneField('NonPlayer', related_name='hc_team')
    owner = models.OneToOneField('NonPlayer', related_name='owner_team')

    class Meta:
        unique_together = ('city', 'nickname')

    def name(self):
        return u' '.join((self.city, self.nickname))

    def __unicode__(self):
        return self.name

class Contract(models.Model):
    team = models.ForeignKey('Team', related_name = 'contracts')
    player = models.ForeignKey('Player', related_name = 'contracts')
    season_start = models.DateField()
    season_end = models.DateField(null=True)
    is_in_force = models.BooleanField()

class StatLine(models.Model):
    """
    http://stats.nba.com/glossary.html
    """
    player = models.ForeignKey('Player', related_name='stats')
    game = models.ForeignKey('Game', related_name='stats')

    mins = models.PositiveSmallIntegerField(
        verbose_name = 'Minutes Played',
        help_text = 'The number of minutes played by a player',
        max_length = 2, 
        default = 0
    )
    fgm = models.IntegerField(
        verbose_name = 'Field Goals Made',
        help_text = 'The number of field goals made, including both \
            two-point and three-point field goals, by a player or team',
        max_length = 2,
        default = 0
    )
    fga = models.IntegerField(
        verbose_name = 'Field Goal Attempted',
        help_text = 'The number of field goals attempted, including both \
            two-point and three-point field goals, by a player or team',
        max_length=2, 
        default=0
    )
    _3pm = models.IntegerField(
        verbose_name = 'Three Pointers Made',
        help_text = 'The number of three-point field goals made',
        max_length=2, 
        default=0
    )
    _3pa = models.IntegerField(
        verbose_name = 'Three Pointers Attempted',
        help_text = 'The number of three-point field goals attempted',
        max_length=2, 
        default=0
    )
    oreb = models.IntegerField(
        verbose_name = 'Offensive Rebounds',
        help_text = 'The number of rebounds collected by the team that \
            attempted the shot',
        max_length=2, 
        default=0
    )
    dreb = models.IntegerField(
        verbose_name = 'Defensive Rebounds',
        help_text = 'The number of rebounds collected by the team that \
            did not attempt the shot',
        max_length=2, 
        default=0
    )
    ast = models.IntegerField(
        verbose_name = 'Assists',
        help_text = 'The number of assists -- passes that lead directly \
            to a made basket -- by a player or team',
        max_length=2, 
        default=0
    )
    stl = models.IntegerField(
        verbose_name = 'Steals',
        help_text = 'The number of steals by a player or team',
        max_length=2, 
        default=0
    )
    blk = models.IntegerField(
        verbose_name = 'Blocks',
        help_text = 'The number of shot attempts that are blocked by a \
            player or team',
        max_length=2, 
        default=0
    )
    tov = models.IntegerField(
        verbose_name = 'Turnovers',
        help_text = 'The number of turnovers -- possessions that are \
            lost to the opposing team -- by a player or team',
        max_length=2, 
        default=0
    )
    pf = models.IntegerField(
        verbose_name = 'Personal Foul',
        help_text = 'The number of personal fouls committed by a player \
            or team',
        max_length=1, 
        default=0
    )
    # TODO: @saul not totally sure about this man
    # might be a good idea to have attributes like
    # `pts` as fields despite redundancy since it 
    # can be a bitch to integrate above-database-level 
    # filtering with libraries and whatnot
    @property
    def pts(self):
        # return self.ftm + 2*self.fgm + 3*self._3pm
        return sum(w*n for w, n in zip(xrange(1, 3), (self.ftm, self.fgm, self._3pm)))

    @property
    def reb(self):
        return self.oreb + self.dreb

    @property
    def per(self):
        # TODO: Insert formula for PER here
        pass

    @property
    def fgrate(self):
        return fgm/float(fga)

    # TODO: define properties for other advanced stats
    # such as 'true field goal %', etc.

    def __unicode__(self):
        return u'PTS {pts} | AST {ast} | REB {reb}'.format(pts=self.pts, \
            ast=self.ast, reb=self.reb)

class Game(models.Model):
    date = models.DateField(verbose_name='Game Date (EST)')
    players = models.ManyToManyField('Player', through='StatLine')
    home = models.ForeignKey('Team', verbose_name='Home Team', related_name='home_games')
    away = models.ForeignKey('Team', verbose_name='Away Team', related_name='away_games')
    # TODO: (or maybe not)
    # officials = models.ManyToManyField('Official')
    # attendance = models.PositiveIntegerField()

    def __unicode__(self):
        # The convention is usually
        # '{home} vs {away}' or '{away} @ {home}'
        # Pick one and roll with it
        return u'{home} vs {away} ({date})'.format(home=self.home, \
            away=self.away, date=self.date)

class Position(models.Model):
    POSITION_CHOICES_DICT = {
        'C': 'Center',
        'PF': 'Power Forward',
        'SF': 'Small Forward',
        'SG': 'Shooting Guard',
        'PG': 'Point Guard',
    }
    name = models.CharField(
        max_length = 2, 
        choices = POSITION_CHOICES_DICT.items(), 
        unique = True
    )