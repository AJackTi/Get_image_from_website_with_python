import urllib2
import urllib
from urllib import urlencode
import urlparse
from bs4 import BeautifulSoup
import json
import mech
text_file = open("imgs.txt", "w")
urls=[]
with open('Output.txt', 'r') as f:
	data = f.readlines()
	# doc nhung dong cua file va dua vao list
	for line in data:
		urls.append(line)

i=0
for x in xrange(0,10):
	ab = mech.anonBrowser(proxies=[],\
		user_agents=[('User-agent', 'superSecretBrowser')])
	website = ab.open(urls[x])
	html = website.read()
	soup = BeautifulSoup(html, "html5lib")
	for img in soup.findAll('img'):
		print img
		text_file.write(str(img))
		print i
		i+=1

print i
text_file.close()
