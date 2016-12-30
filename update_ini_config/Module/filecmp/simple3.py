#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2016-12-25
@author: Administrator

dircmp提供了三个输出报告的方法：
report() ，比较当前制定目录中的内容；
report_partial_closure() ， 比较当前制定目录及第一季子目录中的内容；
report_full_closure() ，递归比较所有制定目录的内容。
'''
import filecmp

dir1="dir1"
dir2="dir2"
dirobj = filecmp.dircmp(dir1,dir2,['test.py'])      #目录比较，忽略test.py文件
# 输出对比结果数据报表，详细说明请参考filecmp类方法及属性信息。
dirobj.report()
dirobj.report_partial_closure()
dirobj.report_full_closure()

print("left_list:" + str(dirobj.left_list))
print("right_list:" + str(dirobj.right_list))
print("common:" + str(dirobj.common))
print("left_only:" + str(dirobj.left_only))
print("right_only:" + str(dirobj.right_only))
print("common_dirs:" + str(dirobj.common_dirs))
print("common_files:" + str(dirobj.common_files))
print("common_funny:" + str(dirobj.common_funny))
print("same_files:" + str(dirobj.same_files))
print("diff_files:" + str(dirobj.diff_files))
print("funny_files:" + str(dirobj.funny_files))








