from bs4 import BeautifulSoup
import urllib2
import urllib
import json
import argparse
import os

def grab_static_file(url):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
	headers = {'User-Agent' : user_agent}
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	body = soup.find('body')
	scrape_body(body)


def scrape_body(body):
	for link in body.find_all('a'):
		if not 'https://www.youtube.com/watch?v=' in link.get('href'):
			continue
		else:
			os.system("python parser.py %s" % (link.get('href')))
	grab_json_data()


def grab_json_data(path):


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('url', help='Enter URL of the static file')
	args = parser.parse_args()
	grab_static_file(args.url)


