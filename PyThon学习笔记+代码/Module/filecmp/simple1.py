#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2016-12-25

@author: Administrator
'''
import filecmp

file1 = "nginx.conf.v1"
file2 = "nginx.conf.v2"
file3 = "nginx.conf.v3"

print(filecmp.cmp(file1, file2))
print(filecmp.cmp(file1, file3))

print(filecmp.cmp(file1, file2, shallow=1))