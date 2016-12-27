#!/usr/bin/env python
# coding:utf-8

import MySQLdb

class mySqlHelper(object):
	
	global connParams
	connParams = dict(host='127.0.0.1',user='root',passwd='root',db='robot')

	def myInsert(self,sqlSentence,sqlParams):
		conn = MySQLdb.connect(**connParams)
		cur = conn.cursor()
		reCount = cur.execute(sqlSentence,sqlParams)
		conn.commit()
		cur.close()
		conn.close()
	def myDelete(self):
		pass
	def myRename(self):
		pass
	def mySelectOne(self,sqlSentence,sqlParams):
		conn = MySQLdb.connect(**connParams)
		cur = conn.cursor()
		reCount = cur.execute(sqlSentence,sqlParams)
		data = cur.fetchone()
		cur.close()
		conn.close()
		return data

	def mySelectAll(self,sqlSentence,sqlParams):
		conn = MySQLdb.connect(**connParams)
		cur = conn.cursor()
		reCount = cur.execute(sqlSentence,sqlParams)
		data = cur.fetchall()
		cur.close()
		conn.close()
		return data


