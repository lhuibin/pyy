#!/usr/bin/env python
# coding:utf-8
'''网银操作模块'''
#1 判断操作存款取现金额是100的倍数
#2 显示详细信息，要从最近开始。列表反转失效待处理

#4 自己不能给自己转账， 转账要检查余额
#5 每月月底自动生成账单功能
import sys

import hashlib, pickle, time, bank_login

#读取用户数据
with open('usr_info.db', 'rb') as f:
	usr_info = pickle.load(f)

#保存日志
def usr_log_save(operate, info, value_op, balance_log):
	usr_info[bank_login.usr_name].append([time.asctime(), operate, info, value_op, balance_log])
	with open('usr_info.db', 'wb') as f:
		pickle.dump(usr_info, f)

#取现
def withdraw(withdraw_amount):
	with open('usr_account.db', 'rb') as f:
		usr_account = pickle.load(f)
	if int(withdraw_amount) < usr_account[bank_login.usr_name][1]:
		usr_account[bank_login.usr_name][1] -= int(withdraw_amount) 
		with open('usr_account.db', 'wb') as f:
			pickle.dump(usr_account, f)
		operate, info, value_op, balance_log = '取现', '            ', '-'+withdraw_amount, usr_account[bank_login.usr_name][1]  
		usr_log_save(operate, info, value_op, balance_log)
	else:
		print('余额不足')

#存款
def save_money(save_amount):
	with open('usr_account.db', 'rb') as f:
		usr_account = pickle.load(f)
	usr_account[bank_login.usr_name][1] += int(save_amount)
	with open('usr_account.db', 'wb') as f:
		pickle.dump(usr_account, f)
	operate, info, value_op, balance_log = '存款', '            ', '+'+save_amount, usr_account[bank_login.usr_name][1]  
	usr_log_save(operate, info, value_op, balance_log)

#转账
def transfer(resver_usr, transfer_amount):
	with open('usr_account.db', 'rb') as f:
		usr_account = pickle.load(f)
	usr_account[bank_login.usr_name][1] -= int(transfer_amount)
	usr_account[resver_usr][1] += int(transfer_amount)
	with open('usr_account.db', 'wb') as f:
		pickle.dump(usr_account, f)
	operate, info, value_op, balance_log = '转账', '收款人：%s' % resver_usr, '-'+transfer_amount, usr_account[bank_login.usr_name][1]  
	usr_log_save(operate, info, value_op, balance_log)
	sender = bank_login.usr_name #当前用户名备份
	bank_login.usr_name = resver_usr #当前用户名赋值给收款人账户，用于使用保存日志函数（此方式不合理）
	operate, info, value_op, balance_log = '收款',  '转账人：%s' % sender, '+'+transfer_amount, usr_account[bank_login.usr_name][1]  
	usr_log_save(operate, info, value_op, balance_log)
	bank_login.usr_name = sender#重新赋值给当前操作用户

#显示详单
def account_list():
	with open('usr_info.db', 'rb') as f:
		usr_info = pickle.load(f)
	usr_list = usr_info[bank_login.usr_name]
	print('|            时间           |  操作 |     备注      |  金额  |  余额  |\n-----------------------------------------------')
	for i in usr_list:
		print(i)

# 选择操作
items = {'1': '取现', '2': '存款', '3': '转账', '4': '查询', '5': '退出'}
print(u'\n    %s，你好！请选择项目：' % bank_login.usr_name)
def op_list():
	print('----------')
	for k, v in items.items():
		print(k, v)
	print('----------')
op_list()
while True:
	usr_input = input('请选择项目编号：')
	if usr_input not in items:
		print('格式错误，请重新输入！')
		continue
	elif usr_input == '1':
		withdraw_amount = input('请输入金额（本机仅提供100面额纸币）：')
		withdraw(withdraw_amount)
		print('取款成功!\n请继续选择:')
		op_list()
	elif usr_input == '2':
		save_amount = input('请放入纸币（本机仅接受100面额纸币）：')
		save_money(save_amount)
		print('存款成功!\n请继续选择:')
		op_list()
	elif usr_input == '3':
		reverse_usr = raw_input('请输入收款人账户：')
		transfer_amount = input('请输入转账金额：')
		transfer(reverse_usr, transfer_amount)
		print('转账成功!\n请继续选择:')
		op_list()
	elif usr_input == '4':
		account_list()
	else:
		exit('欢迎再次光临，再见！')
