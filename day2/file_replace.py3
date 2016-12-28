#!/usr/bin/env python
# coding:utf-8

import sys, os

old_text, new_text, file_name = sys.argv[1], sys.argv[2], sys.argv[3]

new_file = open('%s.bak' % file_name, 'w')

with open(file_name, 'r') as f:
	for i in f.readlines():	
		new_file.write(i.replace(old_text, new_text))
				
new_file.close()

if '--bak' in sys.argv:
	os.rename(file_name, 'bak.%s' % file_name)
	os.rename('%s.bak' % file_name, file_name)
else:
	os.remove(file_name)
	os.rename('%s.bak' % file_name, file_name)