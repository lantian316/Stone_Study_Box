#!/usr/bin/env python
import os
def load_stat():
    loadavg = {}
    f = open("/proc/loadavg")
    conn = f.read().split()
    f.close()
    loadavg['lavg_1']=conn[0]
    loadavg['lavg_5']=conn[1]
    loadavg['lavg_15']=conn[2]
    loadavg['nr']=conn[3]
    loadavg['last_pid']=conn[4]
    return loadavg



print( "loadavg",load_stat()['lavg_15'])