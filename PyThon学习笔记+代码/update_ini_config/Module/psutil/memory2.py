#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import psutil



#内存信息获取
mem = psutil.virtual_memory()
print(mem)

print("内存总数：(GB)：",mem.total/1024/1024/1024,"              内存总数：(MB)：",mem.total/1024/1024)
print("内存剩余：(GB)：",mem.free/1024/1024/1024,"               内存总数：(MB)：",mem.free/1024/1024)


print("内存总数：(GB)：",round(mem.total/1024/1024/1024, 2),"              内存总数：(MB)：",round(mem.total/1024/1024, 2))
print("内存剩余：(GB)：",round(mem.free/1024/1024/1024, 2),"               内存总数：(MB)：",round(mem.free/1024/1024, 2))


print("内存总数：(GB)：",int(mem.total/1024/1024/1024),"              内存总数：(MB)：",int(mem.total/1024/1024))
print("内存剩余：(GB)：",int(mem.free/1024/1024/1024),"               内存总数：(MB)：",int(mem.free/1024/1024))