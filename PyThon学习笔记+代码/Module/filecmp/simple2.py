#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2016-12-25

@author: Administrator
'''
import filecmp

dir1="dir1"
dir2="dir2"

list = filecmp.cmpfiles(dir1, dir2, ['f1','f2','f3.py'])
print(list)
'''
返回一个tuple
分别是3个列表
列表一：匹配的文件
列表二：不匹配的文件
列表三：文件不存在
'''


print(list[0])