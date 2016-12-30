#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import print_function
from collections import OrderedDict

def memeryinfo():
    memeryinfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            memeryinfo[line.split(':')[0]] = line.split(':')[1].strip()
    return memeryinfo

if __name__ == '__main__':
    memeryinfo = memeryinfo()
    print('总共内存:{0}'.format(memeryinfo['MemTotal']))
    print('剩余内存:{0}'.format(memeryinfo['MemFree']))
