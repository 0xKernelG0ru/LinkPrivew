from bs4 import BeautifulSoup
import parser
import urllib2
import urllib

def anaylze_html(url):








if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_arguement('html', help='Enter URL of the static file')
	args = parser.parse_args()
	content = urllib2.urlopen(args.html)
	html = content.read()