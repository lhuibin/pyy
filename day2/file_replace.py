#!/usr/bin/env python
# coding:utf-8
# 这是一个文件内容替换的程序
# 使用格式：python 程序名 old_text new_text file_name --bak

# 可增加改名功能
# 设计成为批量修改文件内容程序。
# 可修改word exl等文件
import sys, os

old_text, new_text, file_name = sys.argv[1], sys.argv[2], sys.argv[3]#获取输入参数 

new_file = open('%s.bak' % file_name, 'w')

with open(file_name, 'r') as f:
	for i in f.readlines():	
		new_file.write(i.replace(old_text, new_text))  #写入替换内容
				
new_file.close()

if '--bak' in sys.argv: #备份
	os.rename(file_name, 'bak.%s' % file_name)
	os.rename('%s.bak' % file_name, file_name)
else:
	os.remove(file_name) 
	os.rename('%s.bak' % file_name, file_name)