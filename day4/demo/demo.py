#!usr/bin/env python
#coding utf-8
'''
model = __import__('account')
func = getattr(model, 'logout')
func()
'''
'''
#通过输入进入不同界面
user_input = input('格式xxx/xxx:\n')
user_input_s = user_input.split('/')
model = __import__(user_input_s[0])
func = getattr(model, user_input_s[1])
func()
'''
'''
#通过输入进入不同界面,不同目录
user_input = input('格式xxx/xxx:\n')
user_input_s = user_input.split('/')
model = __import__('admin.'+user_input_s[0])
func = getattr(model, user_input_s[1])
func()
'''
'''
class foo(object):
	"""dage, nametring for foo"""
	def __init__(self, age, name):
		self.age = age
		self.name = name
	def detail(self):
		print(self.name,':',self.age)

f1 = foo(25, 'lhb')
f2 = foo(16, 'wh')
f1.detail()
f2.detail()
#print(f1.name,f1.age,'\n'+f2.name, f2.age)
'''
'''
class foo(object):
	"""dage, nametring for foo"""
	def __init__(self, age, name, gendar):
		self.age = age
		self.name = name
		self.gendar = gendar
	def detail(self, go):
		print(self.name,',',self.age,',',self.gendar,',', go)

f1 = foo(25, 'lhb', 'male')
f2 = foo(16, 'wh', 'female')

f1.detail('爱看电影')
f2.detail('爱学习')
f1.detail('也爱学习')
f2.detail('有时候也看电影')
'''
class charictor(object):
	"""dage, nametring for foo"""
	def __init__(self, age, name, gendar, start_fight):
		self.age = age
		self.name = name
		self.gendar = gendar
		self.start_fight = start_fight
	def grass(self):
		self.start_fight = self.start_fight  - 200
	def multi_person(self):
		self.start_fight = self.start_fight  - 500
	def exercise(self):
		self.start_fight = self.start_fight  + 100
	def detail(self):
		print(self.name,',',self.age,',',self.gendar,',', self.start_fight)

cang = charictor(28, 'cangjingkong', 'female', 1000)
mumu = charictor(35, 'mumukong', 'male', 1800)
lu = charictor(45, 'luzhishen', 'male', 2500)

cang.detail()
cang.grass()
cang.detail()
cang.exercise()
cang.detail()
mumu.multi_person()
mumu.detail()
lu.exercise()
lu.detail()