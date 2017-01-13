#  -*- coding:utf-8 -*-
from pip._vendor.distlib.compat import raw_input
from builtins import str


def functionname():
    print("hello")
    

def printme(str):
    print(str)

def sum(a,b):
    return a+b

def repeat_str(s,times=1):
    repeated_strs=s*times
    return repeated_strs

print(repeat_str("Happy Birthday!"))
print(repeat_str("Happy Birthday!",4))
functionname()
# printme(raw_input('请输入： '))
print(sum(1, 4))




def func(a,b=4,c=8):
    print("a is ",a,'and b is ',b,'and c is',c)
    
    
func(13,17)
func(a=13,c=54)
func(c=54,a=54564)
print('\n')

def print_paras(fpara,*nums,**words):
    print("fpara:　" + str(fpara))
    print("nums:　" + str(nums))
    print("words:　" + str(words))

print_paras("hello",1,123423,123423,1457,18787,19789,1123,1,word="python",anohter_work="java")
