# -*- coding: utf-8 -*-
# http://webpy.org/cookbook/userauthbasic
# android client: com.example.api.LoginService

import web  
import datetime

import web
import re
import base64

urls = (
    '/','Index',
    '/login','Login'
)

app = web.application(urls,globals())

allowed = (
    ('jon','pass'),
    ('tom','pass')
)


class Index:
    def GET(self):
        if web.ctx.env.get('HTTP_AUTHORIZATION') is not None:
            #return 'This is the index page'
            return '{"username":"u", "password":"p"}'
        else:
            raise web.seeother('/login')

class Login:
    def GET(self):
        auth = web.ctx.env.get('HTTP_AUTHORIZATION')
        authreq = False
        if auth is None:
            authreq = True
        else:
            auth = re.sub('^Basic ','',auth)
            username,password = base64.decodestring(auth).split(':')
            print (username, password)
            if (username,password) in allowed:
                raise web.seeother('/')
            else:
                authreq = True
        if authreq:
            web.header('WWW-Authenticate','Basic realm="Auth example"')
            web.ctx.status = '401 Unauthorized'
            return

if __name__=='__main__':
    app.run()
