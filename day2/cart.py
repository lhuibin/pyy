#!/usr/bin/env python
# coding:utf-8

#列表，字典，集合的应用
#添加一个给字典加序功能，可以按序号选商品，不用输入商品名
#优化代码，不要出错
product = {'apple': 8, 'plane':5000000, 'macbook': 9800, 'iphone':6999, 'car': 690000, 'hours':990000}

wage = input('Please input your sealay:')
buy_b = [] #定义已购买列表

while True:
	for k, v in product.items():
		print("The %s's is %s" % (k, v))
	
	buy = raw_input('Which do you want?')
	price = product[buy]
	
	if buy in product and (wage - price) > 0:
			wage -= price
			buy_b.append(buy)
	else:
		buy_i =set(buy_b) #集合，去重
		print('-----------------------------\nYou had brought:')
		for a in buy_i:
			print(">>> %s %s."% (buy_b.count(a), a))
		if wage>=8:
			print("you can't buy anymore %s, your sealay is %s. please choose others:\n-----------------------------" % (buy,wage))

		else:
			print("you can't buy anymore!")
			exit()
		
	
