import urllib2
import urllib
import re
import urlparse
import os
import os.path

YIDIAN = 'http://www.yidianzixun.com/'

PROXY = True

proxy_param = {}
if PROXY:
	proxy_param = {'http':'http://web-proxy.oa.com:8080'}
proxy_handler = urllib2.ProxyHandler(proxy_param)
opener = urllib2.build_opener(proxy_handler)
r = opener.open(YIDIAN)
print r.code

page = r.read()
r.close()

p = re.compile(r'.*?<div class="section section-hotwords">(.*?</div>)</div>', re.S)
m = p.match(page)
#print m.group(1).decode('utf-8').encode('gbk')

section = m.group(1)
#print section

p = re.compile(r'.*?<li.*?><a href="(.*?)".*?>(.*?)</a></li>')
'''
for m in p.finditer(section):
	print m.group(1).decode('utf-8').encode('gbk')
'''

dict = {}
pos = 0
try:
	while True:
		m = p.match(section, pos)
		title = m.group(2).decode('utf-8').encode('gbk')
		url = urlparse.urljoin(YIDIAN, m.group(1).replace('&amp;', '&'))
		print title, url
		dict[title] = url
		pos = m.end()
except:
	print 'End'
	
#print dict
print 'Generating my news'

if not os.path.exists('tmp'):
	os.mkdir('tmp')
f = file('tmp/my_news.html', 'w')
for (k, v) in dict.items():
	#print k, v
	f.write('<a href="%s" target="_blank">%s</a><br>' % (v, k))

f.close()