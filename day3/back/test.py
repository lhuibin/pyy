'''a = input('please input the name')
counter = 0
while a != '1':
	counter += 1
	if counter<2:
		print('go out')
		a = input('please input the name again! you have %s times!' % (3-counter))
	else:	
		break
else:
	print('welcome')	'''
'''
def foo(a):
	print(a,'foohellop')

def  bar(a):
	print(a,'barhellop')

def function(a):
	if a =='1':
		foo(a)
	else:
		bar(a)
a = input('input:')
function(a)'''
import time
import pickle
usr_account,usr_info,locked_account,shopping_list,product_list = {}, {}, [],{},{}

'''with open('product_list.db', 'wb') as f:
	pickle.dump(product_list, f)'''
with open('shopping_list.db', 'wb') as f:
	pickle.dump(shopping_list, f)




'''with open('usr_account.db', 'wb') as f:
	pickle.dump(usr_account, f)
with open('usr_info.db', 'wb') as f:
	pickle.dump(usr_info, f)
#usr_info['lhb']=[time.asctime(), 'test', 'info', 'value_op', 'balance_log']
with open('locked_account.db', 'wb') as f:
	pickle.dump(locked_account, f)

'''
'''
'''
'''with open('usr_info.db', 'rb') as f:
	a = pickle.load(f)
print(a)
'''