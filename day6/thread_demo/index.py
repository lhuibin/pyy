#!/usr/bin/env python
#coding:utf-8

from threading import Thread 
import time

def foo(arg):
	for i in list(range(5)):
		print(i)
		time.sleep(1)
	 

print('before')
t1 = Thread(target=foo,args=(1,))
t1.setDaemon(True)
t1.start()
t1.join(10)
print(t1.getName() ,'after')
time.sleep(5)