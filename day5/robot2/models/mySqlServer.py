#!/usr/bin/env python
# coding:utf-8

import sys
sys.path.append('..')
from utility.mySqlHelper import mySqlHelper

sql1 = mySqlHelper()

class userInfo(object):
	
	def reg(self):
		usrName = raw_input('Please input the username:')
		passWd = raw_input('Please input the password:')
		sqlSentence,sqlParams = 'insert into userInfo(usrName,passWd) values(%s,%s)',(usrName,passWd)
		sql1.myInsert(sqlSentence,sqlParams)

	def checkUser(self):
		pass

class msgDb(object):
	
	def msgSave(self,msgTime,msgContent,userID):
		sqlSentence,sqlParams = 'insert into msgDb(msgTime,msgContent,userID) values(%s,%s,%s)',(msgTime,msgContent,userID)
		sql1.myInsert(sqlSentence,sqlParams)

	def msgGet(self,userID):
		sqlSentence,sqlParams = 'select * from msgDb where userID=%s',(userID,)
		msgData = sql1.mySelectAll(sqlSentence,sqlParams)
		return msgData