#!usr/bin/env python
# coding:utf-8

'''def login():
	print('welcome!')

def logout():
	print('goodbye!')


	'''
#
# 从log中读取当前最大序号，log文件需要要求/num/
'''def Ord_num():
	with open('log.txt', 'r') as f:
		ord_raw = f.read()
	cont = ord_raw.split('/')
	
	num = []
	for i in cont:
		if len(i) == 1:#这样最大只能到9.如何破
			if 47<ord(i)<58:
				num.append(int(i))
	return max(num)

Ord_num = Ord_num()

print(Ord_num)
'''
'''def Ord_num():
	with open('log.txt', 'r') as f:
		ord_raw = f.read()
	cont = ord_raw.split('/')
	num = []
	for i in cont:
		try:
			i = int(i)
		except TypeError as e:
			pass
		else:
			i = int(i)
			num.append(i)
			print(num)
		finally:
			print(num)
			return num
	return max(num)

'''
# 从log中读取当前最大序号，log文件需要要求/num/

def Ord_num():
	import re
	with open('log.txt', 'r') as f:
		return max(list(map(int,re.findall(r'[\d]+',f.read()))))

Ord_num = Ord_num()
print(Ord_num)