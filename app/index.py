# -*- coding: utf-8 -*-
import web  
import datetime

import raw_request 

from web.wsgiserver import CherryPyWSGIServer

CherryPyWSGIServer.ssl_certificate = "cert/cert.pem"
CherryPyWSGIServer.ssl_private_key = "cert/key.pem"

urls = (  
    '/index', 'Index'         
) 

def cache_valid(cache_time):
    
    '''
    cache_time: 缓存时间
    根据http协议，判断缓存是否失效。如果缓存失效则设置Last-Modified属性，
    否则返回Http响应状态码304 Not Modified
    '''
    last_time_str = web.ctx.env.get('HTTP_IF_MODIFIED_SINCE', '')
    last_time = web.net.parsehttpdate(last_time_str)
    now = datetime.datetime.now()
    if last_time and last_time + datetime.timedelta(seconds = cache_time) > now:
        web.notmodified()
        return True
    else:
        web.lastmodified(now)
        return False

class Index:

    _cache_time = 20
    
    def GET(self):
    
        print raw_request.rawRequest(web.ctx.env)
    
        user_data = web.input(force_refresh='0')
        print 'force_refresh=' + user_data.force_refresh
        if user_data.force_refresh and user_data.force_refresh != '0':
            # web.lastmodified用于设置Last-Modified属性
            web.lastmodified(datetime.datetime.now())
            return '{"data":"' + str(datetime.datetime.now()) + '"}'
        elif not cache_valid(self._cache_time):
            return '{"data":"' + str(datetime.datetime.now()) + '"}'
		
    def POST(self):
        pass
		
app = web.application(urls, globals())  
  
if __name__ == '__main__':  
    app.run()