# -*- coding: utf-8 -*-
# http://webpy.org/cookbook/postbasic
# android client: com.example.api.TaskService
# android client: com.example.api.converter.*

import web
import json
import random

urls = (  
    '/tasks', 'Task'         
) 


class Task:

    def POST(self):
        data = web.data()
        
        # 处理自定义converter
        if '\n' in data:
            return data
        
        o = json.loads(data)
        # 生成随机id
        o['id'] = random.randint(0, 100000)
        ret = json.dumps(o)
        return ret
		
app = web.application(urls, globals())  
  
if __name__ == '__main__':  
    app.run()