#!/usr/bin/env python
# coding:utf_8

# 解决让机器人问候语重复的问题。

import SocketServer,time
from utility.mySqlHelper import mySqlHelper
from models import mySqlServer
from models.robot import Robot 

class Myserver(SocketServer.BaseRequestHandler):

	def handle(self):
		conn = self.request
		conn.send('seri>>>')
		msgTime,msgContent,userID = time.asctime(),conn.recv(1024),1
		msgS = mySqlServer.msgDb()
		msgS.msgSave(msgTime,msgContent,userID)
		msgClient = msgContent
		seri = Robot()
		msgReply = 'seri>>>'+seri.reply(msgClient)
		time.sleep(2) #模拟真人，回复有延迟。优化根据 问题 + 答案的长短决定等待回复时间。
		conn.send(msgReply)

params = ('127.0.0.1',9996)
server = SocketServer.ThreadingTCPServer((params),Myserver)
server.serve_forever()
#this is a test github desktop