#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import configparser

config = configparser.ConfigParser()

config.read('config_file.ini')
#section = input("please enter section:")
#key = input("please enter key:")
#value = input("please enter value:")


#config.set(section,key,value) 
config.set("MYSQLD", "md5", "fuck you..........") 
#第一个是中括号里面的，第二个是key，第三个是需要修改的新值

config.write(open('config_file.ini', "r+"))

print("配置文件更新成功，3秒后自动退出...")
time.sleep(3)