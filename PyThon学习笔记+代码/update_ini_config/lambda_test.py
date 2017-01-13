#!/usr/bin/env python
# -*- coding: utf-8 -*-

def add(a,b):
    return a + b
def multi(a,b):
    return a* b
def sub(a,b):
    return a - b
def div(a,b):
    return a/b#b is non-zero
'''
def calc(type,x,y):
    calculation  = {'+':lambda:add(x,y),
                    '*':lambda:multi(x,y),
                    '-':lambda:sub(x,y),
                    '/':lambda:div(x,y)}
    return calculation[type]()
result1 = calc('+',3,6)
result2 = calc('-',3,6)
print result1, result2
''' 

def calc(type):
    calculation  = {'+':lambda:print(50),
                    '*':lambda:print(100),
                    '-':lambda:print(200),
                    '/':lambda:print(300)}
    return calculation[type]()

calc('+')
calc('-')
