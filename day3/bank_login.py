#!/usr/bin/env python
# coding:utf-8
'''这是登陆模块'''

#1. 要加入数据备份功能
#2. 用户输入密码要求密文
#3. 注册要加入验证可用用户名功能
#4. 
#5. 用户名密码要格式化，用正则表达式限定
#6. 用数据库存储数据
#8. 锁定记录24小时候自动删除
#10. 注册功能仅限银行模块使用
#11. 自动格式化数据库
#12. 处理全局变量改局部变量警告的问题

import hashlib, pickle, time

#读写数据
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
		global usr_info
		with open('usr_info.db', 'wb') as f:
			pickle.dump(usr_info, f)
	elif order=='locked_account_r':
		with open('locked_account.db', 'rb') as f:
 			locked_account = pickle.load(f)
 			return locked_account
	elif order=='locked_account_w':
 		global locked_account
 		with open('locked_account.db', 'wb') as f:
 			pickle.dump(locked_account, f)

#md5加密 加盐
def md5_pwd(usr_name, usr_pwd):
	md5 = hashlib.md5()
	md5.update(str('%s' % usr_name +'%s' + usr_pwd +'581231').encode('utf-8'))
	return md5.hexdigest()

#验证密码
def check_pwd(usr_name, usr_pwd):
	usr_account = r_w_db('usr_account_r')
	usr_pwd_md5 = md5_pwd(usr_name, usr_pwd)
	if usr_name not in usr_account:
		return None
	if usr_pwd_md5 == usr_account[usr_name][0]:
		return True
	else:
		return False

#处理登陆
def lock_account(usr_name, usr_pwd):
	usr_account_id = check_pwd(usr_name, usr_pwd)
	counter = 0
	counter2 =0
	while usr_account_id == None:
		counter2 += 1
		if counter2 < 5:
			print('用户名输入错误，你还有%s次尝试机会!' %(5 - counter2))
			usr_name = input('请重新输入：')
		else:
			print('您的IP已被锁定！请24小时候再次尝试。') #获取客户端IP地址并记录
			exit()
	while usr_account_id == False:
		counter += 1
		if counter < 3:
			print('密码不正确，您今天还有%s次尝试机会!' %(3 - counter))
			usr_pwd = input('请输入密码：')
		else:
			locked_account = r_w_db('locked_account_r')
			locked_account.append(usr_name)
			locked_account = r_w_db('locked_account_w')
			print('账户被锁定，请带上证件去开户行办理密码重置手续')
			exit()
	else:
		return 'done' 

#注册账户
def creat_account(usr_name, usr_pwd, amount=15000):
	usr_pwd_md5 = md5_pwd(usr_name, usr_pwd)
	usr_account = r_w_db('usr_account_r')
	usr_account[usr_name] = [usr_pwd_md5, amount]
	r_w_db('usr_account_w')
	usr_info = r_w_db('usr_info_r')
	usr_info[usr_name]=[[time.asctime(), '开户', '    ', '    ', amount]]
	r_w_db('usr_info_w')
	return ('注册成功!',usr_info)

#修改密码
def pwd_update(usr_name, usr_pwd, new_pwd):
	
	if check_pwd(usr_name, usr_pwd) == True:
		usr_account = r_w_db('usr_account_r')
		new_pwd_md5 = md5_pwd(usr_name, new_pwd)
		usr_account[usr_name] = [new_pwd_md5, usr_account[usr_name][1]]
		usr_account = r_w_db('usr_account_w')
	else:
		lock_account(usr_name, usr_pwd)

# 登陆窗口
usr_name = input('请输入您的账户：')

# 检查账户是否锁
locked_account = r_w_db('locked_account_r')
if usr_name in locked_account:
	print('你的账户已被锁定，请带上证件去开户行办理相关手续')
	exit()
#用户开户入口
if usr_name == 'admin_reg':
	usr_name = input("开户入口.请输入用户账户(大小写字母,'-','_'组合)：")
	usr_pwd = input('开户入口.由用户输入密码：')
	creat_account(usr_name, usr_pwd, amount=15000) #调用管理员开户程序
	exit()

usr_pwd = input('请输入您的密码：')
lock_account(usr_name, usr_pwd) #验证登陆


