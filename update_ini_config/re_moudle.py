#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


some_string = '''\
sql_var_pool_count= 300000
sql_blob_var_pool=100
sql_Execute_pool_count=6000
sql_Execute_noreturn_pool_count=20000
'''
#print(some_string)
it = re.findall(r'sql_var_pool_count', some_string)
it = re.findall(r'(sql_var_pool_count=.*)', some_string)
#it = re.fullmatch(r'sql_var_pool_count=(.*)', some_string)

print('it变量为         ---     ',it[0])
print(type(it))