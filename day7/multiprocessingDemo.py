from multiprocessing import Process
import os
import time

def info(title):
	print title
	print 'module name:', __name__
	if hasattr(os, 'getppid'): #only available on Unix
		print 'parent process:', os.getppid()
	time.sleep(15)
	print 'process id:',os.getpid()

def f(name):
	info('function f')
	print 'hello',name

if __name__== '__main__':
	info('main line')
	print '------------------'
	p = Process(target=f,args=('bob',))
	p.start()
	p.join()

