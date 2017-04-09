#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2017/3/1-15:46.
Author:Stone
Email:lantian316@163.com
企鹅:283302410
'''

score = int(input("Enter an interger: "))

if score >= 90 :
    print("高手")
elif score < 90 or score >= 60 :
    print("一般")
else :
    print("水货")