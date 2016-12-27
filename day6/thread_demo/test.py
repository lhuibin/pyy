#!/usr/bin/env python
#coding:utf-8

from threading import Thread 
import time

class myThread(Thread):
	
	def run(self):
		time.sleep(2)
		print('I am thread.') 
		Thread.run(self)

def foo():
	print 'bar'
t1 = myThread(target = foo)
t1.start()
print('end')
