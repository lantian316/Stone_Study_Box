#  -*- coding:utf-8 -*-
import os
import requests

print(os.getcwd())


print("hello world")
print('hello world')
print('''hello world
         this is a test
         this is last line''')
age=3
name="tom"
print("{0} was {1} years old".format(name, age))
print(name + " was " + str(age) +" years old")


r = requests.get("http://www.163.com")
print(r.url)
print(r.encoding)
# print(r.text)