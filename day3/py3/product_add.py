#!usr/bin/env/ python
# coding:utf-8

'''添加商品'''

# 处理连续增加商品的问题

import time, pickle
#读取信息
def reading_info(order):
	if order=='product_list':
		with open('product_list.db', 'rb') as f:
			product_list = pickle.load(f)
		return product_list
	elif  order=='shopping_list':
		with open('shopping_list', 'rb') as f:
			shopping_list = pickle.load(f)
		return shopping_list
	elif order == 'usr_account':
		with open('usr_account.db', 'rb') as f:
			usr_account = pickle.load(f)
		return usr_account
	elif order == 'usr_info':
		with open('usr_info.db', 'rb') as f:
			usr_info = pickle.load(f)
		return usr_info

#写入信息
def writing_info(order):
	if order=='product_list':
		with open('product_list.db', 'wb') as f:
			pickle.dump(product_list, f)
	elif  order=='shopping_list':
		with open('shopping_list.db', 'wb') as f:
			pickle.dump(shopping_list, f)
	elif order=='usr_account':
		with open('usr_account.db', 'wb') as f:
			pickle.dump(usr_account, f)
	elif order=='usr_info':
		with open('usr_info', 'wb') as f:
			pickle.dump(usr_info, f)

usr = input('请输入您的账户：')
while  True:
	if usr == 'admin_add':
		print('%s, 你好！\n 请选择操作（0：新增商品，1：增加库存，2：修改价格）' % usr)
		p_op = input()
		product_list = reading_info('product_list')
		print(product_list)
		while True:
			if p_op == '0':#新增
				P_name = input('请输入名称：')
				p_amount = input('请输入库存：')
				P_price = input('请输入单价：')
				product_list[P_name] = [p_amount, P_price]
				continue
			elif p_op =='1':#增加库存
				P_name = input('请输入名称：')
				p_amount = input('请输入库存：')
				product_list[P_name] = [product_list[P_name][0]+p_amount, P_price]
			else:
				P_name = input('请输入名称：')
				P_price = input('请输入单价：')
				product_list[P_name] = [product_list[P_name][0], P_price]
			writing_info('product_list')