#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Created on 2016-12-24
description:通过使用difflib模块实现两个字符串的差异对比。采用HTMLDifferent()类的make_file()方法生成美观的html文档
            当我们维护多个nginx配置时，经常会对比不同版本配置文件的差异，了解不同版本迭代后的更新项，读取两个配置文件，然后同上一个例子
@author: Administrator
符号说明：
  '-'  ：包含在第一个序列行中，但不包含该在第二个序列行
  '+'  ：包含在第二个序列行中，但不包含该在第一个序列行 
  ''   ：两个序列行一致
  '?'  ：标志两个序列行存在增量差异
  '^'  ：标志出两个序列行存在的差异字符
'''

import difflib
import sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print("Error:"+ str(e))
    print("Usage: simple3.py filename1 filename2")
    sys.exit()
    
def readfile(filename):
    try:
        fileHandle = open(filename,'r')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print('Read file Error:' + str(error))
        sys.exit()
        
if textfile1 == "" or textfile2 == "":
    print("Usage: simple3.py filename1 filename2")
    sys.exit()
    
text1_lines = readfile(textfile1)
text2_lines = readfile(textfile2)

d = difflib.HtmlDiff()
diff = d.make_file(text1_lines, text2_lines)
print(d.make_file(text1_lines, text2_lines))

'''可以执行脚本将内容重定向输出到 diff.html,然后查看diff.html的内容，有颜色标记，美观。   simple3.py nginx.conf.v1 nginx.conf.v2 > diff.html '''