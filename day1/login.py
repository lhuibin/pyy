#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json

# 读取用户数据
with open('usr_pwd.json', 'r') as f:
	usr_pwd = json.loads(f.read())
with open('usr_locked.json', 'r') as f:
	usr_locked = json.loads(f.read())

# 登陆入口，供用户选择注册新用户或登陆
welcomeInfo = input("Hello! What's do you want? Login(l) or Register(r)")

if welcomeInfo == 'r':
	usrinput_name = input('Please input your username:')
	usrinput_pwd = input('Please input your password:')
	usr_pwd[usrinput_name] = usrinput_pwd #这是一个字典，添加新用户
	with open('usr_pwd.json', 'w') as f:
		f.write(json.dumps(usr_pwd)) #新用户注册数据存储

count1 = 0 #用户名输入次数计数器
count2 = 0 #密码输入次数计数器

# 登陆程序
while welcomeInfo == 'l':
	usr_name = input('Please input your username:')

	with open('usr_locked.json', 'r') as f:  #读取锁定用户数据，判断是否是已锁定用户
		lock_usr = json.loads(f.read())  
		if usr_name in lock_usr: 
			print('Your login is denail! please contract the Administrator')
			break
	
	with open('usr_pwd.json', 'r') as f: #读取用书数据
		n = json.loads(f.read()) 
		
	if n.get(usr_name) == None:  #判断是否是已注册用户
		print('Wrrong username! If you forgot you username, please contract Administrator!')
		count1 += 1
		if count1 >= 5: #如用户名输错5次，警告并结束程序
			print('You are denailed!') # 如果是客户端登陆，获取IP，并记录锁定此IP。（此功能暂未实现）
			break
		continue

	usr_pwd = input('please input your password:')
	if usr_pwd == n[usr_name]:  # 校验密码
		print('Welcome! %s' % usr_name)
		break
	
	else:  # 校验错误，输出错误信息，三次尝试错误后锁定并记录数据
		count2 += 1
		print('Sorry! Your password are wrong. You had %s times!' % (3-count2))
		if count2 >= 3:
			print('Warning! Your account was locked, please contract the Administrator.')
			usr_locked.append(usr_name)
			with open('usr_locked.json', 'w') as f:
				f.write(json.dumps(usr_locked))
			break
		

 
 
