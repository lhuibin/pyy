#!/usr/bin/env python
# coding:utf-8
# 此程序用来初始化需要的数据格式。

import pickle
usr_account,usr_info,locked_account,shopping_list,product_list = {}, {}, [],{},{}

with open('product_list.db', 'wb') as f:
	pickle.dump(product_list, f)
with open('shopping_list.db', 'wb') as f:
	pickle.dump(shopping_list, f)
with open('usr_account.db', 'wb') as f:
	pickle.dump(usr_account, f)
with open('usr_info.db', 'wb') as f:
	pickle.dump(usr_info, f)
#usr_info['lhb']=[time.asctime(), 'test', 'info', 'value_op', 'balance_log']
with open('locked_account.db', 'wb') as f:
	pickle.dump(locked_account, f)
