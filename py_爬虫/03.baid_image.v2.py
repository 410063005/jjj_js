
import re
import urllib2
import urlparse
import os
import os.path

DEBUG = True
PROXY = True

f = file('03.baid_image.txt')
s = f.read()
print type(s)

# Caution! .*? before <div class
# Caution! .*? after img
p = re.compile(r'.*?<div class="img_pic_wrap_layer">(<img.*?)</div>', re.S)
#m = p.match('<div class="img_pic_wrap_layer"><img src="http://a.hiphotos.baidu.com/image/h%3D200/sign=febfa19b4ded2e73e3e9812cb700a16d/f7246b600c338744233d6163560fd9f9d72aa031.jpg"  class="img_pic_layer" /></div>')


pos = 0
img = []

for m in p.finditer(s):
	img.append(m.group(1))
'''
try:
	while True:
		m = p.match(s, pos)
		img.append(m.group(1))
		pos = m.end(1)
except:
	print 'End'
'''
#if DEBUG: print '\n'.join(img)
	
src = []
p = re.compile(r'<img src="(.*?)".*')
for i in img:
	m = p.match(i)
	src.append(m.group(1))
if DEBUG: print '\n'.join(src)

proxy_handler = None
if PROXY:
	proxy_handler = urllib2.ProxyHandler({'http':'http://web-proxy.oa.com:8080'})
else:
	proxy_handler = urllib2.ProxyHandler({})
	
opener = urllib2.build_opener(proxy_handler)

if not os.path.exists('tmp'):
	os.mkdir('tmp')

for s in src:
	r = opener.open(s)
	path = urlparse.urlparse(r.geturl())[2]
	pos = path.rfind('/')
	name = path[pos+1:]
	print r.code, name
	f = file('tmp/' + name, 'wb')
	f.write(r.read())
	r.close()