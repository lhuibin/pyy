#!usr/bin/env python
# coding:utf-8

# class' ziduan
'''class Province:
	"""docstring for Province"""
	#jingtai ziduan
	memo = 'one of the 23 Province of China'
	def __init__(self, name, capital):
		#dongtai ziduan
		self.n = name
		self.c = capital
sh = Province('shanghai','sh')
js = Province('jiangsu','nj')
print(sh.n,sh.c)
print(js.n,js.c)
		
# class' xiaohui
class foo:
	"""docstring for foo"""
	def __init__(self,):
		pass
		print('beginning')
	def __del__(self):
		print('I will be died soon...')
	def go(self):
		print('go')

#a = foo()
#a.go()
#a'''

# class' @property
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.n = name
		self.s = score

	def get(self):
		return self._s

	def set(self,value):
		if not isinstance(value,int):
			raise ValueError('you must be input an integer!')
		if value>100 or value<0:
			raise ValueError('you must input the value between 0 - 100!')
		self._s = value


s1 = Student('wanghui',100)
s1.set(99)
print(s1.n, s1._s,s1.s)
