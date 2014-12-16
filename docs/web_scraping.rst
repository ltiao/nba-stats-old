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

##############
Scrapy Crawler
##############

Scrapy gives you a number of ways to specify the URLs from which to start
crawling. Typically, a list of `start_urls <http://doc.scrapy.org/en/latest
/topics/spiders.html#scrapy.spider.Spider.start_urls>`_ are specified and by
default, `start_requests <http://doc.scrapy.org/en/latest/topics/spiders.html#scrapy
.spider.Spider.start_requests>`_ will use `make_requests_from_url <http://
doc.scrapy.org/en/latest/topics/spiders.html#scrapy.spider.Spider.
make_requests_from_url>`_ to generate `Request <http://doc.scrapy.org/en/
latest/topics/request-response.html#scrapy.http.Request>`_ objects from the URLs.

While our starting URLs don't require authentication so no ``POST`` requests are 
required, they are however, parameterized. Therefore, we override ``start_requests`` 
and return (an iterator of) ``FormRequest`` object(s) with the starting URL and
the required parameters.

.. include:: resource_details.rst

###########################
NBA Statistics Terms of Use
###########################

From http://www.nba.com/news/termsofuse.html#statistics:

  "The Operator of this Site may make available on this Site statistics, including statistics generated and/or calculated by the Operator using proprietary calculations and analyses, relating to or arising out of the performance of players during or in connection with NBA, Women’s National Basketball Association (“WNBA”) or NBA Development League (“D-League”) games, competitions or events (collectively, “NBA Statistics”). By using such NBA Statistics, you agree that: (1) any use, display or publication of the NBA Statistics shall include a prominent attribution to NBA.com in connection with such use, display or publication; (2) the NBA Statistics may only be used, displayed or published for legitimate news reporting or private, non-commercial purposes; (3) the NBA Statistics may not be used in connection with any sponsorship or commercial identification; (4) the NBA Statistics may not be used or referred to in connection with any gambling activity (including legal gambling activity); (5) the NBA Statistics may not be used in connection with any fantasy game or other commercial product or service; (6) the NBA Statistics may not be used in connection with any product or service that presents a live, near-live or other real-time or archived play-by-play account or depiction of any NBA game; and (7) the NBA Statistics may not be used in connection with any web site, product or service that features a database (in any medium or format) of comprehensive, regularly updated statistics from NBA, WNBA or D-League games, competitions or events without the Operator’s express prior consent." 