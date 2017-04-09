#!/usr/bin/env python
# -*- coding: UTF-8 -*-

f=open('file_write.txt','w')         # r只读，w可写，a追加
for i in range(0,10):
    f.write(str(i)+'\n')
f.close()