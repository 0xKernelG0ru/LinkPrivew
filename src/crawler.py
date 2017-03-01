from bs4 import BeautifulSoup
import parser
import urllib2
import urllib
import json

def grab_static_file(url):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'
	headers = {'User-Agent' : user_agent}
	req = urllib2.Request(url, None, headers)
	response = urllib2.urlopen(req)
	html = response.read()










if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_arguement('html', help='Enter URL of the static file')
	args = parser.parse_args()
	grab_static_file(url)


