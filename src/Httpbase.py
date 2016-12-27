#coding: utf-8
'''
Created on 2016年12月22日

@author: Jane Wei
'''

import time
import socket
import httplib

class Http(object):
    def __init__(self, host='qixun.ckingiot.com', port=80, path='/', method='GET', params=None):
        self.host = host
        self.path = path
        self.method = method.upper()
        self.params = params
        if port == '':
            self.port = 80
        else:
            self.port = port

    def request(self,isHttp=1):
        if isHttp:
            print('http://' + self.host + self.path)
        else:
            print('https://' + self.host + self.path)
        try:
            headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Connection': 'Keep-Alive',
                             'Accept': 'text/plain'}
            # params = urllib.parse.urlencode(self.params)
            if isHttp:
                conn = httplib.HTTPConnection(self.host,self.port)
            else:
                conn = httplib.HTTPSConnection(self.host,self.port)
            start_time = time.time()
            #print self.path, self.params, headers
            conn.request(method=self.method, url=self.path, body=self.params, headers=headers)
            response = conn.getresponse()
            data = response.read()
            #objs = json.loads(data)
            end_time = time.time()
            conn.close()
            return response.status,response.reason,data,end_time-start_time
        
        except Exception,e: #socket.error
                #print(socket.error)
                print(e)
                conn.close()
                return 0,Exception,''
            
        finally:
            conn.close()
