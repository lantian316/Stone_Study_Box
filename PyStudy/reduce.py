# -*- coding: utf-8 -*-
from functools import reduce

'''
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def fn(x, y):
    return x * 10 + y

L = map(char2num, '1')
print(L)
print(map(char2num, '13579'))
print(reduce(fn,map(char2num, '2897475286489347')))


def a(l):
    for i in l:
        print(i)
        
'''
#a('123')



'''
def c2n(one):
    dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return dict[one]

def forlist(str):
    sum=0
    for i in str:
        sum=sum+c2n(i)
    return sum

print(forlist('9876892364762374982637846'))

'''

'''
def normalize(name):
    return name.lower().capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
'''

'''
def sum1(a,b):
    return a * b

L1 = [1,2,3,4,5,6]
print(reduce(sum1, L1))
'''


def str2float(float_str):
    list = float_str.split('.')
    (lfloat_str, rfloat_str) = float_str.split('.')
    
    def char2num(num_char):
        dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,'5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        c = dict[num_char]
        return c

    def func(x, y):
        return x * 10.0 + y

    
    a = reduce(func, map(char2num, list[0]))
    b = reduce(func, map(char2num, list[1])) / 10 ** len(list[1])
    c = a + b
    print(a)
    print(b)
    print(c)
    return reduce(func, map(char2num, list[1])) + reduce(func, map(char2num, list[1])) / 10 ** len(list[1])

print(str2float('235.123'))
print(10**4)


str='654654.5454'
list=str.split('.')
print(list)







