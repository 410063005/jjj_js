# -*- coding: utf-8 -*-
# http://webpy.org/cookbook/storeupload/
# android client: com.example.api.TaskService
# android client: com.example.api.converter.*

import web
import json
import random

urls = (  
    '/upload', 'Upload'         
) 


class Upload:
    def GET(self):
            return """<html><head></head><body>
    <form method="POST" enctype="multipart/form-data" action="">
    <input type="file" name="myfile" />
    <br/>
    <input type="submit" />
    </form>
    </body></html>"""

    def POST(self):
        #print web.data()
        x = web.input(myfile={})
        if 'myfile' in x:
            print x.myfile
            fout = file('c:\\' + x.myfile.filename + '-' + str(random.randint(0, 100000)), 'wb')
            fout.write(x.myfile.file.read())
            fout.close()
            return "{'error':0}"
        
        return "{'error':1}"
		
app = web.application(urls, globals())  
  
if __name__ == '__main__':  
    app.run()