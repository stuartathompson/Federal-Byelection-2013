import urllib
import re
import csv
from BeautifulSoup import BeautifulSoup
import ftplib
from threading import Timer
import json
import mechanize

#connect to FTP
session = ftplib.FTP('######','YYYYYYY','XXXXXXX')
session.cwd('') #Enter publishing URL

#mechanize publisher
br = mechanize.Browser()
user = 'YYYYYYY'
pwd = 'XXXXXXXX'
br.addheaders = [('User-agent', 'Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)')]
url = "" # Enter Publishing URL
br.add_password(url,user,pwd)
r = br.open(url)

urls = [
    'http://enr.elections.ca/ElectoralDistricts.aspx?ed=1432&lang=e',
    'http://enr.elections.ca/ElectoralDistricts.aspx?ed=1468&lang=e',
    'http://enr.elections.ca/ElectoralDistricts.aspx?ed=1220&lang=e',
    'http://enr.elections.ca/ElectoralDistricts.aspx?ed=1227&lang=e'
    ]
    
ridings = [
	'1432', #Toronto
	'1468', #Bourassa
	'1220', #Brandon
	'1227' #Provencher
];
header = {
	'riding':'riding',
	'party':'party',
	'candidate':'candidate',
	'votes':'votes',
	'percent':'percent',
	'polls':'polls',
	'turnout':'turnout'
}
filename = 'fed-byelection-results'

brow = mechanize.Browser()
response = brow.open("http://enr.elections.ca/ElectoralDistricts_e.aspx")
print response.read()

def publishFile():
	print "publishing file..."
	br.select_form(nr=0)
	br.form['desc'] = 'pythonupdate'
	br.form.find_control(name="dir").items[0].selected=True
	response = br.submit()
	for link in br.links():
		if link.url == "": # ENTER PUBLISHING URL
			print "found!"
			response = br.follow_link(link)
			r = br.open(url)
			html = r.read()
			print "done!"

def uploadFile():
    file = open('%s.js' % filename,'rb')
    session.storbinary('STOR %s.js' % filename,file)
    file.close()

def saveData(output):
	with open('%s.js' % filename,'w') as outfile:
		outfile.write("var results=")
		json.dump(output,outfile)
		print "Done!"

def getData():
	print "fetching data"
	select_form['ddlElectoralDistrict'] = "1432"
	print "go"
	output = []
	output.append(header)
	x=-1
	for url in urls:
		x=x+1
		print ridings[x]
		#print "Now scraping from %s..." % (url)
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html, convertEntities=BeautifulSoup.HTML_ENTITIES)
		containers = soup.find('div',id=re.compile('^divResultucElectoralDistrictResult[0-9]*'))
		polls = soup.find('span',id=re.compile('^litPollsReportingValueucElectoralDistrictResult[0-9]*')).getText().encode('ascii','ignore')
		turnout = soup.find('span',id=re.compile('^litVoterTurnoutValueucElectoralDistrictResult[0-9]*')).getText().split(' registered electors')[0].encode('ascii','ignore')
		for table in containers.findAll('table',id=re.compile('^grdResultsucElectoralDistrictResult[0-9]*')):
			rows = table.findAll('tr')[1:]
			i=-1
			for row in rows:
				i=i+1
				if(i<len(rows)):
					tds = row.findAll('td')
	    			output.append({
	    				'riding':ridings[x],
    					'party':tds[0].getText(),
    					'candidate':tds[1].getText(),
	    				'votes':tds[2].getText(),
    					'percent':tds[3].getText(),
    					'polls':polls,
    					'turnout':turnout
    				})
	#saveData(output) #save all data for this year
	#uploadFile()
	#publishFile()
	print "Successfully scraped all URLs, uploaded and published"
	Timer(15.0,getData).start()

t = Timer(1.0,getData).start()