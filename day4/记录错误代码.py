#!usr/bin/env python
# coding:utf-8

'''import demo2

a = input('Please input address(format:XX/XX) >>')
array = a.split('/')
print(array)

if a == 'demo2/login':
	demo2.login()
if a =='demo2/logout':
	demo2.logout()
#else:
#	print('your input is wrong!')
'''
'''# 装饰器
def func(func):
	def lhb():
		print('excute %s!' % func.__name__)
		func()
	return lhb

@func
def foo():
	print('I am foo!')

foo()
'''
#装饰带参数的函数
'''def func(func):
	def ss(arg):
		print('execute %s!' % func.__name__)
		func(arg)
	return ss

@func
def bar(arg):
	print('I am %s !' % arg)

bar('hello')
'''
'''# 带可变参数的装饰器
def wra(function):
	def wrapper(*arg,**args):
		print('execute %s!' % function.__name__)
		return function(*arg,**args)
	return wrapper

@wra
def foo(*arg,**args):
	#for a in arg:
	#	print(a)
	#print('hello, %s %s %s' % (*arg))
	for i, v in args.items():
		print(i, v)

score = {'lhuibin': 98, 'wanghui':100, 'liuxiu':100}
name = 'sutdent'
name2 = 1
foo(name,name2,**score)
'''

#import functools
'''#带参数的装饰器
def log(arg1):
	def wra(func):
		@functools.wraps(func)
		def wrapper(*arg, **args):
			#wrapper.__name__ = func.__name__
			print('%s %s' % (arg1,func.__name__))
			return func(*arg,**args)
		return wrapper
	return wra

@log('exute')
def foo():
	print('I am %s' % foo.__name__)

foo()
'''
'''def log(*text):
	def wra(func):
		@functools.wraps(func)
		def wrapper(*arg,**args):
			print('%s call begin' % func.__name__)
			func(*arg,**args)
			print('%s call end' % func.__name__)
		return wrapper
	return wra

@log()
def f():
	print('I am %s' % f.__name__)

f()'''
'''以下是记录错误日志的代码'''
#有待实现简化调用，最好能载入模块，就能调动此功能

# 从log中读取当前记录的序号，以便于追加记录
def Ord_num():
	import re
	with open('log.txt', 'r') as f:
		return max(list(map(int,re.findall(r'[\d]+',f.read()))))

#记录错误
import logging

def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s)*2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
		global Ord_num
		Ord_num = int(Ord_num()) + 1
		with open('log.txt', 'a+') as f:
			f.write(str(Ord_num)+'. '+str(e)+'\n')

main()
print('END')