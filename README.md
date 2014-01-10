Federal-Byelection-2013
=======================

A live-udpating tally of federal byelection results.

Coding, layout and scraping (in Python) by Stuart A. Thompson

See the live version here: http://www.theglobeandmail.com/news/politics/live-results-from-toronto-centre-and-three-other-federal-byelections/article15587457/#dashboard/follows/

About this project
------

While Elections Canada typical provides a live feed of election results, they do not provide this service for by-elections. I wanted a way to provide live results for readers interested in following the tally online. 

The process was complicated. First, I needed to create a scraper that could pull results from the Elections Canada website. Then I needed to get them online. But the Globe's internal publishing system requires you first FTP your content then manually publish it to the live site. Since I wanted everything automated, I wrote another function in Python (using Mechanize) that could complete this manual publishing process.

On the front end, I used jQuery to fetch the results and parse them, and Raphael.js to present bar charts. A separate file of winners was used to signal when someone secured the riding.
