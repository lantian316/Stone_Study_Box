#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

print("系统默认编码为：",sys.getdefaultencoding())

hanzi = input("输入吧骚年：")
assert isinstance(hanzi, object)
print(hanzi)