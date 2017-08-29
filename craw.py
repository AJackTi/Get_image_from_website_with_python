import urllib
import urlparse
from bs4 import BeautifulSoup
import json
url = 'http://wallpaperswide.com/'
urls = [url]
visited = [url] # da duyet roi
kq = [url]
text_file = open("Output.txt", "w")

while len(urls)>0:
	try:
		html = urllib.urlopen(urls[0]).read()
	except:
		print urls[0]
	soup = BeautifulSoup(html, "html.parser")
	urls.pop(0)
	print len(urls)
	if len(visited)>100:
		text_file.close()
		break
	
	for tag in soup.findAll('a', href=True):
		tag['href'] = urlparse.urljoin(url, tag['href'])
		if url in tag['href'] and tag['href'] not in visited:
			x=tag['href'].encode('utf-8','ignore')
			# print x
			if len(x)>20:
				text_file.write(x+"\n")
				kq.append(tag['href'])
			urls.append(tag['href'])
			visited.append(tag['href'])
text_file.close()