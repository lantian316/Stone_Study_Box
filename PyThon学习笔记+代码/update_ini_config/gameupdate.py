#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import configparser


path="D:\\python_update_test\\"
dir_list=["hdx_server_2","hdx_server_3"]


#server_list=["BackServer","DBServer","GameServer","GateServer","LogServer","ValidateServer"]
server_list=["ValidateServer","DBServer","GameServer","GateServer"]

for dir in dir_list:
    for server in server_list:
        #print(path+dir+"\\"+server+"\\win32\\ServerConfig.ini")
        fullconfigpath=path+dir+"\\"+server+"\\win32\\ServerConfig.ini"
        
        if server=="ValidateServer":
            config = configparser.ConfigParser()
            config.read(fullconfigpath)
            config.set("MysqlDBConfig","sql_var_pool_count","300000")
            config.set("MysqlDBConfig","sql_blob_var_pool","2000")
            config.set("MysqlDBConfig","sql_Execute_pool_count","6000")
            config.set("MysqlDBConfig","sql_Execute_noreturn_pool_count","2")
            config.write(open(fullconfigpath, "r+"))
        elif server=="DBServer":
            print('oh no,你猜的太低了')
        elif server=="GameServer":
            print('oh no,你猜的太低了')
        elif server=="GateServer":
            print('oh no,你猜的太低了')
            
#这个方法不行，会把注释全部清除掉。

'''
config = configparser.ConfigParser()

config.read('config_file.ini')
section = input("please enter section:")
key = input("please enter key:")
value = input("please enter value:")


config.set(section,key,value) 
#config.set("MYSQLD", "md5", "fuck you..........") 
#第一个是中括号里面的，第二个是key，第三个是需要修改的新值

config.write(open('config_file.ini', "r+"))
config.clear()
print("配置文件更新成功，3秒后自动退出...")
time.sleep(3)'''