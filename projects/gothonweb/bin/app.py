# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 20:28:43 2017

@author: Administrator
"""

import web

urls = (
        '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        greeting = "hello world"
        return greeting
    
if __name__ == "__main__":
    app.run()