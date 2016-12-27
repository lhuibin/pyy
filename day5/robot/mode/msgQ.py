#!/usr/bin/env python
# coding:utf_8

import sys
sys.path.append("..")
from utility.mySqlHelper import mySqlHelper

class msgQ(object):
	msgSelect = mySqlHelper()
	global msgData
	msgData = msgSelect.select()[::-1]
	def handle(self):
		for msg in msgData:
			print(msg[1]+' >>> '+msg[2])
