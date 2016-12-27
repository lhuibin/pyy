#!usr/bin/env python
# coding:utf-8

def foo(**a):
	for x, y in a.items():

		print(x,y)
	return a

a = foo(x =2,y =1, z=2,d='a')
print(a)
