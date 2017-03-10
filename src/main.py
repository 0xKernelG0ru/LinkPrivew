from bs4 import BeautifulSoup
import urllib2
import argparse
from datetime import datetime, timedelta
from threading import Timer
import subprocess
import threading



#The function takes the given url and extract the body from the HTML code of the site.
#A User-Agent is used in case of 403 case.
def grab_static_file(url):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
	headers = {'User-Agent' : user_agent}
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	body = soup.find('body')
	scrape_body(body)

	


#The code here takes the body that was extraced and then search for links in it,
#if a found link contains a YouTube URL pattern, then the parser script is run over it.
def scrape_body(body):
	for link in body.find_all('a'):
		if not 'https://www.youtube.com/watch?v=' in link.get('href'):
			continue
		else:
			t = threading.Thread(target=subprocess.call('python scrape.py %s' % (link.get('href'))))
			t.daemon = True
			t.start()
			
	
#The clean_up function works anytime the script is called. Though, it will clean up the log only if, 
#have been two hours since the last clean-up.	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('url', help='Enter URL of the static file')
	args = parser.parse_args()
	grab_static_file(args.url)
	
	
	



