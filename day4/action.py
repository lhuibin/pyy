#!/usr/bin/env python
# coding:utf-8

#defined human
class Person(object):
	"""docstring for person"""
	def __init__(self,*args):
		for i in args:
			self.i = i

#argsPeter = ['name','age','gender','height','weight','education','property','occupation']
Peter = Person()
Peter.name = 'Peter'
Peter.age = 38

print(Peter.name,':',Peter.age)