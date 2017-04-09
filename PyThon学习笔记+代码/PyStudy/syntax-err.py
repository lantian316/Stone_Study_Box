#  -*- coding:utf-8 -*-

#Example of syntax errors
# while 1:
#     print("hello world")
    
#Examples ofexceptions
# print(8/0)
#print(hello * 4)
# num=6
# print("hello world" + num)

#handling exceptions
# while 1:
#     try:
#         x = int(input("please enter a number: "))
#         break
#     except ValueError:
#         print("you enter not number,try again...")
# print(x)

try:
    f=open('myfile.txt')
    s=f.readline()
    i=int(s.strip())
except OSError as err:
    print("OS error:{0}".format(err))
except ValueError :
    print("could not convert data to an int.")





