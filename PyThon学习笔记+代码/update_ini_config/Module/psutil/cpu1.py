#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import psutil


print(psutil.cpu_times())                #显示cpu的整个信息
print(psutil.cpu_times().user)
print(psutil.cpu_count())                #获取cpu的逻辑个数(核心)
print(psutil.cpu_count( logical=False ))



print(psutil.swap_memory())
print(psutil.disk_io_counters())
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
print(psutil.disk_io_counters(perdisk=True))
print()
print()
print()
print()
print()
print()
#print(psutil.pids())
p=psutil.Process(10024)
print(p.name())
print(p.exe())          #进程的bin路径
print(p.cwd())          #进程的工作目录绝对路径
print(p.status())          #进程状态
print(p.create_time())          #进程创建时间
#print(p.uids())           #进程uid信息
#print(p.gids())          #进程的gid信息
print(p.cpu_times())          #进程的cpu时间信息,包括user,system两个cpu信息
print(p.cpu_affinity())          #get进程cpu亲和度,如果要设置cpu亲和度,将cpu号作为参考就好
print(p.memory_percent())          #进程内存利用率
print(p.memory_info())          #进程内存rss,vms信息
print(p.io_counters())          #进程的IO信息,包括读写IO数字及参数
#print(p.connectios())          #返回进程列表
print(p.num_threads())          #进程开启的线程数