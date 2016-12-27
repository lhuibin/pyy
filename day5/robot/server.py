#!/usr/bin/env python
# coding:utf_8

import SocketServer
import sys,time
sys.path.append("..")
from utility.mySqlHelper import mySqlHelper


msg1 = mySqlHelper()

class Myserver(SocketServer.BaseRequestHandler):
	def setup(self):
		pass
	def handle(self):
		conn = self.request
		conn.send('hello')
		da = conn.recv(1024)
		ti = time.asctime()
		#print(ti,da)
		cont = (ti,da)
		msg1.insert(cont)

params = ('127.0.0.1',9999)
server = SocketServer.ThreadingTCPServer((params),Myserver)
server.serve_forever()
