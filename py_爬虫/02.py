# -*- coding: UTF-8 -*-

import requests
import re


url = "http://www.heibanke.com/lesson/crawler_ex01/"

for i in range(1, 31):
	r = requests.post(url, data = {"csrfmiddlewaretoken":"kwQb2WWgTOQffEwKPnK4EJ2rfnK9mfzE", "username": "username", "password": i})
	if u"您输入的密码错误, 请重新输入" not in r.text:
		print '' + str(i) + ' OK' 
		break
	else:
		print '' + str(i) + ' Error'
	