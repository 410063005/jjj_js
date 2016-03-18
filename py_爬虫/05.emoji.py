import urllib2
import urllib
import re
import urlparse
import os
import os.path

EMOJI_URL = 'http://apps.timwhitlock.info/emoji/tables/unicode'

PROXY = True

proxy_param = {}
if PROXY:
	#proxy_param = {'http':'http://proxy.tencent.com:8080'}
	proxy_param = {'http':'http://web-proxy.oa.com:8080', 'https':'https://web-proxy.oa.com:8080'}

def get_from_net(url=EMOJI_URL):
	proxy_handler = urllib2.ProxyHandler(proxy_param)
	opener = urllib2.build_opener(proxy_handler)
	r = opener.open(url)
	print r.code

	page = r.read()
	r.close()
	#print page
	return page

def parse_page(page):
	ic_dir = 'twitter'
	if not os.path.exists(ic_dir):
		os.mkdir(ic_dir)

	p = re.compile(r'.*?<img class="emoji twitter"\s+data-src="(.*?)"\s+/>', re.S)
	start = 0
	try:
		while True:
			m = p.match(page, start)
			ic_url = m.group(1)
			print 'ic_url=' + ic_url
			#url = urlparse.urljoin(YIDIAN, m.group(1).replace('&amp;', '&'))
			ic_file = file(ic_dir + '\ic_' + ic_url.split('/').pop(), 'wb')
			ic_file.write(get_from_net(ic_url))
			ic_file.close()

			start = m.end()
	except:
		print 'End'

if __name__ == '__main__':
	'''out = file('emoji.html', 'w')
	out.write(get_from_net())
	out.close()
	'''
	infile = file('emoji.html')
	page = infile.read()
	infile.close()
	parse_page(page)
