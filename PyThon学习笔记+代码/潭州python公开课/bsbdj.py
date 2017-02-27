#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2016/12/29-02:31.
Author:Stone
Email:lantian316@163.com
企鹅:283302410
'''

import tkinter

# Tkinter (capitalized) refers to versions <3.0.
# tkinter (all lowecase) refers to versions ≥3.0
import tkinter.scrolledtext
import tkinter.messagebox
# Note
# ScrolledText has been renamed to tkinter.scrolledtext in Python 3.
# The 2to3 tool will automatically adapt imports when converting your sources to Python 3.
import urllib
import urllib.request
import re
import threading
import os
import sys
#import tkinter.constants
# from tkinter import *
# 注意两种导入写法的不同

a = 1 # 网页页数
def gethtml():
    global a
    hd = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    url = 'http://cli.im/url?e663925dc2db11749fb558ce58550792' + str(a)
    varl.set('已经获取到第%s页视频'%(a))
    req = urllib.request.Request(url,headers=hd)
    print(req)
    openweb2 = urllib.request.urlopen(req)
    html = openweb2.read().decode()
    a = a + 1
    url_content = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)
    url_contents = re.findall(url_content,html)
    url_name = []
    for i in url_contents:
        url_reg = r'data-mp4="(.*?)">'   #地址匹配
        url_items = re.findall(url_reg,i)
        if url_items:
            name_reg = re.compile(r'<a href="/detail-.{8}\.html">(.*?)</a>',re.S)
            name_items = re.findall(name_reg,i)    #名字的集合
            for i,k in zip(name_items,url_items):
                url_name.append([i,k])
                print(i,k)
    return url_name


    #print(url_contents)

id = 1  #视频个数
def write():
    global id
    while id < 100:   # 如果需要爬取更多，请修改这个参数
        url_name = gethtml()   # url + name
        for i in url_name:
            urllib.request.urlretrieve(i[1],'video\\%s.mp4' %(i[0]))
			# 3.x 默认是utf-8 ，好像这里可以不用转码
            # urllib.request.urlretrieve(i[1],'video\\%s.mp4' %(i[0].decode('utf-8').encode('gbk')))
            # 下载到video目录，手工创建一个
            text.insert(tkinter.constants.END,str(id)+'.'+i[1]+'\n'+i[0]+'\n')
            # https://hg.python.org/cpython/file/3.5/Lib/tkinter/scrolledtext.py
            # 关于这个END参数，参考这里发现需要导入以上模块
            url_name.pop(0)
            id = id + 1
    varl.set("拉取完毕，可以去撸了。。。。")

def start():
    th = threading.Thread(target=write)
    th.start()


if not os.path.exists('video'):
    os.mkdir('video')
# 如果下载目录不存在，就创建一个video目录
    
root = tkinter.Tk()
#root.geometry('800x600+200+100')
#设置窗体弹出时的大写和坐标
root.title('来啊，好污的视频，哈哈，开始爬视频啦...')
text = tkinter.scrolledtext.ScrolledText(root,font=('微软雅黑',10),width=97)
# width指定ScrolledText的宽度
text.grid()

button = tkinter.Button(root,text='开始爬取',font=('微软雅黑',10),command=start)
button.grid()

varl = tkinter.StringVar()
label = tkinter.Label(root , font=('微软雅黑',10) , fg='red' , textvariable = varl)
label.grid()
varl.set('快快上车老司机要开车了...')

tkinter.messagebox.showinfo('下载目录信息：', message='小视频下载到脚本同级目录的video目录里面，请知晓')
# 弹出窗口告知下载目录信息

'''
tkinter.messagebox.showwarning('警告信息：', message='警告信息')
tkinter.messagebox.showerror('警告信息：', message='警告信息')
tkinter.messagebox.askokcancel('警告信息：', message='警告信息')
tkinter.messagebox.showinfo('警告信息：', message='警告信息')
'''
root.mainloop()