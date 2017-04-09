#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Update_Config
#from Replace_file_str import *

def __init__(self,path,server_dir_list,server_list):
    self.__path = path
    self.__server_dir_list = server_dir_list
    self.__server_list = server_list

def switch_case(type):
    update_config = Update_Config.Update_Config(path,server_dir_list,server_list)
    calculation  = {'50':lambda:update_config.Update50(),
                    '100':lambda:print(100),
                    '200':lambda:print(200),
                    '400':lambda:print(300)}
    calculation[type]()

path="D:\\python_update_test\\"
server_dir_list=["hdx_server_2","hdx_server_3"]

#server_list=["BackServer","DBServer","GameServer","GateServer","LogServer","ValidateServer"]
server_list=["ValidateServer","DBServer","GameServer","GateServer"]

#number_list = ["50","100","200","300","500","800","1000","1500","2000"]
number_list = [50,100,200,300,500,800,1000,1500,2000]



print("服务器人数配置修改，请输入一下数字，例如输入 50 ，将修改为  50 人配置......      ")
print(number_list)
print()
select = input('服务器配置修改为多少人: ')
print("您选择了将服务器人数配置修改为 %s 人" %(select))
for i in number_list:
    if i == int(select):
        switch_case(select)
        break


'''
def switch_case(type):
    update_config = Update_Config.Update_Config(path,server_dir_list,server_list)
    calculation  = {
        '50':lambda:update_config.Update50(),
        '100': lambda: print(100),
        '200': lambda: print(200),
        '400': lambda: print(300),
    }
    return calculation[type]()



if __name__ == '__main__':
    Update_Config.Update_Config(path,server_dir_list,server_list).Update50()
'''