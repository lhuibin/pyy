#!/usr/bin/env python
# coding=utf-8

'''购物模块'''

# 1.  查询使用可变参数，修改商品 价格设置为可选

import pickle
import time

#读取信息
def reading_info(order):
	if order=='product_list':
		with open('product_list.db', 'rb') as f:
			product_list = pickle.load(f)
		return product_list
	elif  order=='shopping_list':
		with open('shopping_list.db', 'rb') as f:
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
			pickle.dump(order, f)
	elif  order=='shopping_list':
		with open('shopping_list.db', 'wb') as f:
			pickle.dump(order, f)
	elif order=='usr_account':
		with open('usr_account.db', 'wb') as f:
			pickle.dump(order, f)
	elif order=='usr_info':
		with open('usr_info', 'wb') as f:
			pickle.dump(order, f)

# 添加修改商品
'''def add_product(p_op, P_name, p_amount='100', P_price): 
	reading_info('product_list')
	if p_op == '0':#新增
		product_list[P_name] = [p_amount, P_price]
	elif p_op =='1':#增加库存
		product_list[P_name] = [product_list[P_name][0]+p_amount, P_price]
	else:
		product_list[P_name] = [product_list[P_name][0], P_price]
	writing_info('product_list')'''

# 商品列表
def print_shopping_list():
	product_list = reading_info('product_list')
	for k, v in product_list.items():
		print(k, v[0], v[1])

# 购物车
def shopping_list_func(p_name, s_amount):
	with open('shopping_list.db', 'rb') as f:
		shopping_list = pickle.load(f)
	if p_name in shopping_list:
		shopping_list[p_name] += s_amount
	else:
		shopping_list[p_name] = s_amount
	with open('shopping_list.db', 'wb') as f:
		pickle.dump(shopping_list, f)


# 查看购物车 和计算
def shppping_list_check():
	shopping_list = reading_info('shopping_list')
	product_list = reading_info('product_list')
	total_value = 0
	for k, v in shopping_list.items():
		total_value += int(product_list[k][1])*v
		print(k, v, product_list[k][1], int(product_list[k][1])*v)
	print('总计：', total_value)
	return total_value

# 结算
def function():
	shppping_list_check()
	usr_account = reading_info('usr_account')
	usr_account[usr_name][1] -= total_value
	operate, info, value_op, balance_log = 'pay', '    shopping oneline     ', '-'+total_value, usr_account[usr_name][1]  
	usr_log_save(operate, info, value_op, balance_log)

#欢迎信息
print('welcome! Please choose the producters:\n------------------------------------\n|  name  |  stock  |  price  |')
print_shopping_list()
usr_input = raw_input('Producters(name quantity):').split()
p_name, s_amount = usr_input[0], int(usr_input[1])
shopping_list_func(p_name, s_amount)
shppping_list_check()








