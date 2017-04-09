#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import Replace_file_str
#from Replace_file_str import *

class Update_Config(object):
    
    def __init__(self,path,server_dir_list,server_list):
        self.__path = path
        self.__server_dir_list = server_dir_list
        self.__server_list = server_list
    
    def Update50(self):
        rep_file_str = Replace_file_str.Replace_file_str
        for server_dir in self.__server_dir_list:
            for server in self.__server_list:
                #print(path+server_dir+"\\"+server+"\\win32\\ServerConfig.ini")
                fullconfigpath=self.__path+server_dir+"\\"+server+"\\win32\\ServerConfig.ini"
                print("fullconfigpath               =          %s"%fullconfigpath)
                #if __name__ == '__main__':
                #rep_file_str = Replace_file_str.Replace_file_str(fullconfigpath, "sql_var_pool_count","100000")
                #file_content = rep_file_str.get_file_content()
                #print(file_content)
                if server=="ValidateServer":
                    #print("ValidateServer")
                    rep_file_str(fullconfigpath,"sql_var_pool_count","1000000").write_content_to_file()
                    #Replace_file_str.Replace_file_str(fullconfigpath,"sql_var_pool_count","10000000").write_content_to_file()
                    rep_file_str(fullconfigpath,"sql_blob_var_pool","100").write_content_to_file()
                    rep_file_str(fullconfigpath,"sql_Execute_pool_count","6000").write_content_to_file()
                    rep_file_str(fullconfigpath,"sql_Execute_noreturn_pool_count","20000").write_content_to_file()
                    continue
                elif server=="DBServer":
                    #print("DBServer")
                    #Replace_file_str.Replace_file_str(fullconfigpath,"loginmaxsec","20").write_content_to_file()
                    rep_file_str(fullconfigpath,"sql_var_pool_count","366700").write_content_to_file()
                    rep_file_str(fullconfigpath,"sql_blob_var_pool","2400").write_content_to_file()
                    rep_file_str(fullconfigpath,"sql_Execute_pool_count","8700").write_content_to_file()
                    a = "listensql_Execute_noreturn_pool_count_port"
                    rep_file_str(fullconfigpath, a , "6700").write_content_to_file()
                    continue
                elif server=="GameServer":
                    #print("GameServer")
                    rep_file_str(fullconfigpath,"PlayerNum","100").write_content_to_file()
                    continue
                elif server=="GateServer":
                    #print("GateServer")
                    rep_file_str(fullconfigpath,"Login_connect_max","50").write_content_to_file()
                    rep_file_str(fullconfigpath,"PlayerNum","50").write_content_to_file()
                    continue
            print(server_dir+"      50人配置               " + "修改完成......")
            time.sleep(1)
        
        print("配置文件更新成功，3秒后自动退出...")
        time.sleep(3)

    def Update100(self):
        rep_file_str = Replace_file_str.Replace_file_str()
        for server_dir in self.__server_dir_list:
            for server in self.__server_list:
                # print(path+server_dir+"\\"+server+"\\win32\\ServerConfig.ini")
                fullconfigpath = self.__path + server_dir + "\\" + server + "\\win32\\ServerConfig.ini"
                print("fullconfigpath               =          %s" % fullconfigpath)
                # if __name__ == '__main__':
                # rep_file_str = Replace_file_str.Replace_file_str(fullconfigpath, "sql_var_pool_count","100000")
                # file_content = rep_file_str.get_file_content()
                # print(file_content)
                if server == "ValidateServer":
                    # print("ValidateServer")
                    rep_file_str(fullconfigpath, "sql_var_pool_count", "1000000").write_content_to_file()
                    # Replace_file_str.Replace_file_str(fullconfigpath,"sql_var_pool_count","10000000").write_content_to_file()
                    rep_file_str(fullconfigpath, "sql_blob_var_pool", "100").write_content_to_file()
                    rep_file_str(fullconfigpath, "sql_Execute_pool_count", "6000").write_content_to_file()
                    rep_file_str(fullconfigpath, "sql_Execute_noreturn_pool_count", "20000").write_content_to_file()
                    continue
                elif server == "DBServer":
                    # print("DBServer")
                    # Replace_file_str.Replace_file_str(fullconfigpath,"loginmaxsec","20").write_content_to_file()
                    rep_file_str(fullconfigpath, "sql_var_pool_count", "366700").write_content_to_file()
                    rep_file_str(fullconfigpath, "sql_blob_var_pool", "2400").write_content_to_file()
                    rep_file_str(fullconfigpath, "sql_Execute_pool_count", "8700").write_content_to_file()
                    a = "listensql_Execute_noreturn_pool_count_port"
                    rep_file_str(fullconfigpath, a , "6700").write_content_to_file()
                    continue
                elif server == "GameServer":
                    # print("GameServer")
                    rep_file_str(fullconfigpath, "PlayerNum", "100").write_content_to_file()
                    continue
                elif server == "GateServer":
                    # print("GateServer")
                    rep_file_str(fullconfigpath, "Login_connect_max", "50").write_content_to_file()
                    rep_file_str(fullconfigpath, "PlayerNum", "50").write_content_to_file()
                    continue
            print(server_dir + "      50人配置               " + "修改完成......")
            time.sleep(1)

        print("配置文件更新成功，3秒后自动退出...")
        time.sleep(3)