import urllib2
import re

#url = "http://www.baidu.com"

url = "http://www.heibanke.com/lesson/crawler_ex00/"
path = '96911/'
while True:
	newurl = url + path

	request = urllib2.Request(newurl)
	response = urllib2.urlopen(request)

	#lines = response.readlines()
	#print lines
	page = response.read().decode('utf-8')
	#print page
	
	#pattern = re.compile('<h3>(.*)</h3>')
	#result = pattern.match(page)
	#print result.group()
	try:
		h3_start = page.index('<h3>')
		h3_end = page.index('</h3>')
		# print h3_start, h3_end
		line = page[h3_start + 4 : h3_end]
		pattern = re.compile('.*?(\d+).*?')
		result = pattern.match(line)
		path = result.group(1)
		#break
		print url + path
	except:
		print 'Error'
		break
		
print 'End'


'''
C:\>C:\Users\kingcmchen\Desktop\01.py
http://www.heibanke.com/lesson/crawler_ex00/30965
http://www.heibanke.com/lesson/crawler_ex00/67917
http://www.heibanke.com/lesson/crawler_ex00/22213
http://www.heibanke.com/lesson/crawler_ex00/72586
http://www.heibanke.com/lesson/crawler_ex00/48151
http://www.heibanke.com/lesson/crawler_ex00/53639
http://www.heibanke.com/lesson/crawler_ex00/10963
http://www.heibanke.com/lesson/crawler_ex00/65392
http://www.heibanke.com/lesson/crawler_ex00/36133
http://www.heibanke.com/lesson/crawler_ex00/72324
http://www.heibanke.com/lesson/crawler_ex00/57633
http://www.heibanke.com/lesson/crawler_ex00/91251
http://www.heibanke.com/lesson/crawler_ex00/87016
http://www.heibanke.com/lesson/crawler_ex00/77055
http://www.heibanke.com/lesson/crawler_ex00/30366
http://www.heibanke.com/lesson/crawler_ex00/83679
http://www.heibanke.com/lesson/crawler_ex00/31388
http://www.heibanke.com/lesson/crawler_ex00/99446
http://www.heibanke.com/lesson/crawler_ex00/69428
http://www.heibanke.com/lesson/crawler_ex00/34798
http://www.heibanke.com/lesson/crawler_ex00/16780
http://www.heibanke.com/lesson/crawler_ex00/36499
http://www.heibanke.com/lesson/crawler_ex00/21070
http://www.heibanke.com/lesson/crawler_ex00/96749
http://www.heibanke.com/lesson/crawler_ex00/71822
http://www.heibanke.com/lesson/crawler_ex00/48739
http://www.heibanke.com/lesson/crawler_ex00/62816
http://www.heibanke.com/lesson/crawler_ex00/80182
http://www.heibanke.com/lesson/crawler_ex00/68171
http://www.heibanke.com/lesson/crawler_ex00/45458
http://www.heibanke.com/lesson/crawler_ex00/56056
http://www.heibanke.com/lesson/crawler_ex00/87450
http://www.heibanke.com/lesson/crawler_ex00/52695
http://www.heibanke.com/lesson/crawler_ex00/36675
http://www.heibanke.com/lesson/crawler_ex00/25997
http://www.heibanke.com/lesson/crawler_ex00/73222
http://www.heibanke.com/lesson/crawler_ex00/93891
http://www.heibanke.com/lesson/crawler_ex00/29052
http://www.heibanke.com/lesson/crawler_ex00/72996
http://www.heibanke.com/lesson/crawler_ex00/73999
http://www.heibanke.com/lesson/crawler_ex00/23814
http://www.heibanke.com/lesson/crawler_ex00/98084
http://www.heibanke.com/lesson/crawler_ex00/51103
http://www.heibanke.com/lesson/crawler_ex00/39603
http://www.heibanke.com/lesson/crawler_ex00/34316
Error
End
'''