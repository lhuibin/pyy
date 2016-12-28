#!usr/bin/env python
# coding:utf-8
'''import pickle
def r_w_db(order):
	if order == 'usr_account_r':
		with open('usr_account.db', 'rb') as f:
			usr_account = pickle.load(f)
		return usr_account
	elif order=='usr_account_w':
		global usr_account #在python的函数中和全局同名的变量，如果你有修改变量的值就会变成局部变量，在修改之前对该变量的引用自然就会出现没定义这样的错误了，如果确定要引用全局变量，并且要对它修改，必须加上global关键字。
		with open('usr_account.db', 'wb') as f:
			pickle.dump(usr_account, f)
	elif order == 'usr_info_r':
		with open('usr_info.db', 'rb') as f:
			usr_info = pickle.load(f)
		return usr_info
	elif order=='usr_info_w':
		with open('usr_info', 'wb') as f:
			pickle.dump(usr_info, f)
	elif order=='locked_account_r':
		with open('locked_account.db', 'rb') as f:
 			locked_account = pickle.load(f)
 			return locked_account
	elif order=='locked_account_w':
 		with open('locked_account.db', 'wb') as f:
 			pickle.dump(locked_account, f)


locked_account = r_w_db('locked_account_r')
print('locked',locked_account)
locked_account.append('lhb')
r_w_db('lodked_account_w')
print('locked',locked_account)

usr_account=r_w_db('usr_account_r')
print(usr_account)
usr_account['lhuibin'] = [1]

r_w_db('usr_account_w')
print('usr',usr_account)'''

def r_w_db(arg,order):
	if order == 'usr_accountR':
		with open(arg+'.db', 'rb') as f:
			arg = pickle.load(f)
		print(arg)
		return arg

r_w_db()