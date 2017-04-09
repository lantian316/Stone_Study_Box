#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on 2016/12/28-12:33.
@author: 石头(stone)
'''

def printall(object):
    print(object)

def print1(object):
    print("hello world")

def print2(object):
    print("hello python")

def switch_case(type):
    calculation  = {
        '50' : lambda : printall(type),
        '100': lambda : printall(type),
        '200': lambda : print1(type),
        '400': lambda : print2(type),
    }
    #return calculation[type]()
    calculation[type]()

switch_case(str(50))
switch_case(str(100))
switch_case(str(200))
switch_case(str(400))

