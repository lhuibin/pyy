#!/usr/bin/env python
# coding:utf-8

import MySQLdb

class mySqlHelper(object):
	global params
	params = dict(host='127.0.0.1',user='root',passwd='root',db='robot')

	def insert(self,cont):
		conn = MySQLdb.connect(**params)
		cur = conn.cursor()
		reCount = cur.execute('insert into content(time,msg) values(%s,%s)',cont)
		conn.commit()
		cur.close()
		conn.close()
	def delete(self):
		pass
	def rename(self):
		pass
	def select(self):
		conn = MySQLdb.connect(**params)
		cur = conn.cursor()
		reCount = cur.execute('select * from content')
		data = cur.fetchall()
		cur.close()
		conn.close()
		return data


