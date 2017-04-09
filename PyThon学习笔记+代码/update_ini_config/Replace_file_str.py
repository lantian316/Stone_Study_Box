#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time

class Replace_file_str(object):
    
    def __init__(self,file_name,match_str,new_value):
        self.__file_name = file_name
        self.__match_str = match_str
        self.__new_value = new_value
    
    def get_file_name(self):
        return self.__file_name
    
    def set_file_name(self,file_name):
        self.__file_name = file_name
        
    def get_match_str(self):
        return self.__match_str
    
    def set_match_str(self,match_str):
        self.__match_str = match_str
    
    def get_old_str(self):
        return self.search()[0]
    
    def get_new_str(self):
        return self.__match_str +"=" + self.__new_value
    
    def get_file_content(self):
        configfile = open(self.__file_name,"r")#打开配置文件
        filecontent = configfile.read()#读取配置文件所有内容
        configfile.close()
        return filecontent
    
    def write_content_to_file(self):
        file_new_content = self.update_file_in_memory()
        configfile = open(self.__file_name,"w")
        configfile.write(file_new_content)
        configfile.close()
        
    def update_file_in_memory(self):
        #print(self.get_old_str())
        #print(self.get_new_str())
        file_old_content = self.get_file_content()
        #print(file_old_content)
        #print()
        file_new_content = file_old_content.replace(self.get_old_str(),self.get_new_str())
        #print(file_new_content)
        return file_new_content
        
    
    def search(self):
        filecontent = self.get_file_content()#通过自定义方法获取文件内容
        mymatchlist = re.findall(r'(%s.*?.*)'%(self.get_match_str()), filecontent)
        #mymatchlist = re.findall(r'(sql_var_pool_count.*)', filecontent)
        return mymatchlist
'''
        if len(mymatchlist) != 1 :
            print("匹配项不唯一，请检查配置文件或者手工修改配置文件，程序5秒之后自动退出。")
            print("警告："+self.get_file_name()+" 老值："+self.get_old_str()+" 新值："+self.get_new_str())
            #这里可以做日志处理，记录文件路径和文件名，记录修改前的这部分内容，如果确认修改，记录修改后的内容，后续好进行排查
            #time.sleep(5)
            return mymatchlist
        elif len(mymatchlist) == 1 :
            return mymatchlist
'''
        
    
    
#fullconfigpath="D:\python_update_test\hdx_server_2\ValidateServer\win32\ServerConfig.ini"
#rpfs = Replace_file_str(fullconfigpath,"sql_var_pool_count","300000")
#rpfs.write_content_to_file()
#search_list = rpfs.search("sql_blob_var_pool")
#print(rpfs.search("sql_Execute_pool_count")[0])
#print(rpfs.search("sql_Execute_noreturn_pool_count")[0])
#print(rpfs.search("sql_var_pool_count"))

#Replace_file_str(fullconfigpath,"sql_var_pool_count","300000").write_content_to_file()
#Replace_file_str(fullconfigpath,"sql_blob_var_pool","2000").write_content_to_file()
#Replace_file_str(fullconfigpath,"sql_Execute_pool_count","600").write_content_to_file()
#Replace_file_str(fullconfigpath,"sql_var_pool_count","2000000").write_content_to_file()



