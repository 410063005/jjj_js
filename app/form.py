# -*- coding: utf-8 -*-

# android client: com.example.api.FormDataService

import web

urls = (  
    '/form', 'Form'         
) 


class Form:

    def POST(self):
        #data = web.data()
        x = web.input(name='', favors=[])
        print x.name, x.favors
        return '{"error":0, "message":"ok"}'
		
app = web.application(urls, globals())  
  
if __name__ == '__main__':  
    app.run()