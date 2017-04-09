#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print("系统默认编码为：",sys.getdefaultencoding())
sys.getdefaultencoding()
hanzi = input('请输入hanzi:')
print(hanzi)
print(type(hanzi))

#print(name.decode('utf-8'))
#decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
print(hanzi.encode(encoding='utf-8', errors='strict').decode('utf-8'))
#encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
#print(name.encode)