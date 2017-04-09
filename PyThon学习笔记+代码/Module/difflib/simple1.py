#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2016-12-24
description:通过使用difflib模块实现两个字符串的差异对比。
@author: Administrator
符号说明：
  '-'  ：包含在第一个序列行中，但不包含该在第二个序列行
  '+'  ：包含在第二个序列行中，但不包含该在第一个序列行 
  ''   ：两个序列行一致
  '?'  ：标志两个序列行存在增量差异
  '^'  ：标志出两个序列行存在的差异字符
'''

import difflib
# 定义字符串1
text1 = """tex1:   
This module provides classes and functions for comparing sequences.
including HTML and context and unified diffs.
difflib cocument v7.4
aaabbb
add String
"""

text1_lines = text1.splitlines()  # 以行进行分隔，一遍进行对比

# 定义字符串2
text2 = """tex2:   
This module provides classes and functions for Comparing sequences.
including HTML and context and unified diffs.
difflib cocument v7.5
aaabbb
"""
text2_lines = text2.splitlines()

d = difflib.Differ()               # 创建Differ()对象
diff = d.compare(text1_lines, text2_lines)   # 采用 compare方法对字符串进行比较

print('\n'.join(list(diff)))