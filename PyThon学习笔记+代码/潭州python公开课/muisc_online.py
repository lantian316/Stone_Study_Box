#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2016/12/30-15:39.
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

def music():
    if not entry.get():
        tkinter.messagebox.showinfo('温馨提示：', message='您可以输入以下内容进行搜索:\n1.歌曲名\n2.歌手名\n3.部分歌词')



root = tkinter.Tk()
root.geometry('1200x600+200+100')
#设置窗体弹出时的大写和坐标
root.title('在线音乐播放器...')
entry = tkinter.Entry(root)
entry.pack()
button = tkinter.Button(root,text='开始搜索',font=('微软雅黑',10),command=music)
button.pack()

listbox1 = tkinter.Listbox(root,font=('微软雅黑',10),width=97)
# width指定ScrolledText的宽度
listbox1.pack()

root.mainloop()   # 显示窗口

