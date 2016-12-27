#!/usr/bin/env python
# coding:utf_8

import socket
from models.mySqlServer import msgDb
ip_port = ('127.0.0.1',9996)

while True:
	cl = socket.socket()
	cl.connect(ip_port)
	data = cl.recv(1024)
	print(data)
	inp = raw_input('%s>>>' % 'lhb')
	cl.sendall(inp)
	data2 = cl.recv(1024)
	print(data2)
	cl.close()
	userID = 1
	# 查询记录
	if inp == 'check msg':
		msg = msgDb()
		msgData = msg.msgGet(str(userID))[::-1]
		for i in msgData:
			print(i[1]+' >>> '+i[2])
	if inp == 'exit':
		exit()



