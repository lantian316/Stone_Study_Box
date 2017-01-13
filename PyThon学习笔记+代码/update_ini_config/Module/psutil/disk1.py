#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import psutil


#磁盘信息获取
disk = psutil.disk_partitions()
print(disk)
print("C盘使用情况： ",psutil.disk_usage('C:\\'))
print("D盘使用情况： ",psutil.disk_usage('D:\\'))
print("E盘使用情况： ",psutil.disk_usage('E:\\'))
print("F盘使用情况： ",psutil.disk_usage('F:\\'))
print(psutil.disk_io_counters())