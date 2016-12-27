#!/usr/bin/env python
# coding:utf_8

import socket
ip_port = ('127.0.0.1',9999)

while True:
	cl = socket.socket()
	cl.connect(ip_port)
	data = cl.recv(1024)
	print(data)
	inp = raw_input('Client:')
	cl.sendall(inp)
	cl.close()
	if inp == 'exit':
		exit()

#消息查询模块编写完毕，待调用。