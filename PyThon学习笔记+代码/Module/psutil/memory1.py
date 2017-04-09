#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import psutil
#内存信息获取
mem = psutil.virtual_memory()
print(mem)
print('总共内存(MB):{0}'.format(round(mem.total/1024/1024, 2)))
print('总共内存(MB):{0}'.format(round(mem.free/1024/1024, 2)))