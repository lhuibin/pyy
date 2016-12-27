#!/usr/bin/env python
# coding:utf-8

product = {'apple': 8, 'macbook air': 9800, 'iphone':6999, 'car': 690000, 'gril':990000}

wage = int(input('Please input your sealay:'))
buy_b = []

while True:
	for k, v in product.items():
		print("The %s's is %s" % (k, v))
	
	buy = input('Which do you want?')
	price = product[buy]
	
	if buy in product and (wage - price) > 0:
			wage -=price
			buy_b.append(buy)
	else:
		buy_i =set(buy_b)
		if wage>=8:
			for a in buy_i:
				print("You had brought %s %s, and cann't buy anymor %s. your balence is %s, please choose other produce"% (buy_b.count(a), a, a, wage))
		else:
			#print("You had brought %s %s, and cann't buy anymore. your balence is %s"% (buy_b.count(a), a, wage))
			break
		
	
