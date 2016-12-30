#  -*- coding:utf-8 -*-
import psutil
from psutil import disk_io_counters

#cpu信息获取
print(psutil.LINUX)
print(psutil.WINDOWS)
print(psutil.os)
print(psutil.users())
print(psutil.pids())
print(psutil.cpu_stats())
print("cpu_time is: ",psutil.cpu_times())
print("cpu是　",psutil.cpu_count(),"核心！")
print("此机器有",psutil.cpu_count(logical=False),"个物理cpu")

#内存信息获取
mem = psutil.virtual_memory()
print(mem)
print(mem.total)
print(mem.free)

#磁盘信息获取
disk = psutil.disk_partitions()
print(disk)
print("C盘使用情况： ",psutil.disk_usage('C:\\'))
print("D盘使用情况： ",psutil.disk_usage('D:\\'))
print("E盘使用情况： ",psutil.disk_usage('E:\\'))
print("F盘使用情况： ",psutil.disk_usage('F:\\'))
print(psutil.disk_io_counters())


#网络信息
print(psutil.net_io_counters())
print(psutil.net_io_counters(pernic=True))

#其他系统信息
print(psutil.users())
print(psutil.boot_time())





