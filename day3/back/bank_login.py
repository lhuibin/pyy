#!/usr/bin/env python
# coding:utf-8
'''这是登陆模块'''

#1. 要加入数据备份功能
#2. 用户输入密码要求密文
#3. 注册要加入验证可用用户名功能
#4. 增加用户名判定不存在，提供重新输入功能
#5. 用户名密码要格式化，用正则表达式限定

import hashlib, pickle, time
#读取用户数据
with open('usr_account.db', 'rb') as f:
	usr_account = pickle.load(f)
with open('locked_account.db', 'rb') as f:
	locked_account = pickle.load(f)
with open('usr_info.db', 'rb') as f:
	usr_info = pickle.load(f)

#md5加密 加盐
def md5_pwd(usr_name, usr_pwd):
	md5 = hashlib.md5()
	md5.update(str('%s' % usr_name +'%s' + usr_pwd +'581231').encode('utf-8'))
	return md5.hexdigest()

#验证密码
def check_pwd(usr_name, usr_pwd):
	with open('usr_account.db', 'rb') as f:
		usr_account = pickle.load(f)
	usr_pwd_md5 = md5_pwd(usr_name, usr_pwd)
	if usr_name not in usr_account:
		print('用户名不存在！')
		exit()
	if usr_pwd_md5 == usr_account[usr_name][0]:
		return True
	else:
		return False

#处理登陆
def lock_account(usr_name, usr_pwd):
	usr_account_id = check_pwd(usr_name, usr_pwd)
	counter = 0
	while usr_account_id == False:
		counter += 1
		if counter < 3:
			print('Your account information is worng, you have %s time to try!' %(3 - counter))
			usr_pwd = input('请输入密码：')
		else:
			locked_account.append(usr_name)
			with open('locked_account.db', 'wb') as f:
				pickle.dump(locked_account, f)
			print('账户被锁定，请带上证件去开户行办理密码重置手续')
			exit()
	else:
		return 'done' 


#注册账户
def creat_account(usr_name, usr_pwd, amount=15000):
	usr_pwd_md5 = md5_pwd(usr_name, usr_pwd)
	usr_account[usr_name] = [usr_pwd_md5, amount]
	with open('usr_account.db', 'wb') as f:
		pickle.dump(usr_account, f)
	usr_info[usr_name]=[[time.asctime(), '开户', '    ', '    ', amount]]
	with open('usr_info.db', 'wb') as f :
		pickle.dump(usr_info, f)

	return print('注册成功!')

#修改密码
def pwd_update(usr_name, usr_pwd, new_pwd):
	
	if check_pwd(usr_name, usr_pwd) == True:
		with open('usr_account.db', 'rb') as f:
			usr_account = f.pickle.load(f)
		new_pwd_md5 = md5_pwd(usr_name, new_pwd)
		usr_account[usr_name] = [new_pwd_md5, usr_account[usr_name][1]]
		with open('usr_account.db', 'wb') as f:
			pickle.dump(usr_account, f)
	else:
		lock_account(usr_name, usr_pwd)
	



# 登陆窗口
usr_name = input('请输入您的账户：')

# 检查账户是否锁
with open('locked_account.db', 'rb') as f:
	if usr_name in pickle.load(f):
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


