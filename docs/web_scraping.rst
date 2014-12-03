*******************
Web Data Extraction
*******************

While an abundance of data can be retrieved from NBA.com's 
internal and proprietary data sources, any dependency on this  
is inevitably a precarious one, since its developers are under 
no obligation to maintain and document a consistent interface, 
and modifications can be made abruptly at the whim of its developers.

Here, we implement a system of checks which will detect any 
changes in schema, required parameters, etc. and also highlight
and document any peculiarities with the internal interface.

########
Synopsis
########

Most data sources reside in the subdomain http://stats.nba.com
and live under the ``/stats`` directory. e.g. http://stats.nba.com/stats/playerprofile

When querying without parameters, a ``400`` status code will be invoked
and a message of the form::

	LeagueID is required; PlayerID is required; Season is required; 
	SeasonType is required; The GraphStartSeason property is required.; 
	The GraphEndSeason property is required.; The GraphStat property is required.

will be returned, which lists the required parameters. Notice 
that the text for required parameters are somewhat different, i.e.

* ``The <param> property is required.``
* ``<param> is required``

although they are all joined be semicolons (;). At first glance, 
it might appear straightforward to parse this by splitting by
by semicolon. However, this will prove cumbersome since the messages
are potentially heterogeneous. It may be easier to use ``re.findall`` on
the following regular expression::

	(?:The\s)?([A-Za-z]+)\s(?:property\s)?is\srequired

which will extract a list of parameters from the message.

""""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/playergamelog
""""""""""""""""""""""""""""""""""""""""

Required Parameters:

* PlayerID
* Season
* SeasonType

"""""""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/commonallplayers
"""""""""""""""""""""""""""""""""""""""""""

Required Parameters:

* LeagueID
* Season
* IsOnlyCurrentSeason

""""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/playerprofile
""""""""""""""""""""""""""""""""""""""""

Required Parameters:

* LeagueID
* PlayerID
* Season
* SeasonType
* GraphStartSeason
* GraphEndSeason
* GraphStat

"""""""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/commonplayerinfo
"""""""""""""""""""""""""""""""""""""""""""

Required Parameters:

* PlayerID

"""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/playbyplay
"""""""""""""""""""""""""""""""""""""

Required Parameters:

* GameID
* StartPeriod
* EndPeriod

""""""""""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/leaguedashteamstats
""""""""""""""""""""""""""""""""""""""""""""""

Required Parameters:

* MeasureType
* PerMode
* PlusMinus
* PaceAdjust
* Rank
* Season
* SeasonType
* Outcome
* Location
* Month
* SeasonSegment
* DateFrom
* DateTo
* OpponentTeamID
* VsConference
* VsDivision
* GameSegment
* Period
* LastNGames

""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/teamgamelog
""""""""""""""""""""""""""""""""""""""

Required Parameters:

* TeamID
* Season
* SeasonType

"""""""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/commonteamroster
"""""""""""""""""""""""""""""""""""""""""""

Required Parameters:

* Season
* TeamID

""""""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/teamdashlineups
""""""""""""""""""""""""""""""""""""""""""

Required Parameters:

* GroupQuantity
* GameID
* SeasonType
* TeamID
* MeasureType
* PerMode
* PlusMinus
* PaceAdjust
* Rank
* Season
* Outcome
* Location
* Month
* SeasonSegment
* DateFrom
* DateTo
* OpponentTeamID
* VsConference
* VsDivision
* GameSegment
* Period
* LastNGames

"""""""""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/boxscoreadvanced
"""""""""""""""""""""""""""""""""""""""""""

Required Parameters:

* GameID
* StartPeriod
* EndPeriod
* StartRange
* EndRange
* RangeType

"""""""""""""""""""""""""""""""""""""
http://stats.nba.com/stats/scoreboard
"""""""""""""""""""""""""""""""""""""

Required Parameters:

* GameDate
* LeagueID
* DayOffset

