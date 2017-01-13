#  -*- coding:utf-8 -*-

number_tuple=(1,3,5,7,9)
string_tuple=("what","java",7878,343)
print("tuple: "+str(number_tuple))

print(""+ str(number_tuple.index(1)))
print(""+ str(number_tuple[1]))

print("{0}{1}{2}".format(string_tuple[0], string_tuple[1],string_tuple[2]))

print("number_tuple",len(number_tuple))
# number_tuple(1)=18
# string_tuple(2)="lkjskdf"

print("tuple: "+str(number_tuple))
print("tuple: "+str(string_tuple))
add_tuple=(number_tuple+string_tuple)
print("tuple: "+str(add_tuple))

print(len((1,2,3,4,5)))
print((1,2,3,4,5)+(6,7,8,9,10))
print(('hello') * 4)
print(5 in (1,2,3,4))

abcd_tuple = ('a','b','c','d')
print(abcd_tuple[1])
print(abcd_tuple[-2])
print(abcd_tuple[1:])
print(abcd_tuple[2:])
print(abcd_tuple[:3])



a_tuple=(2,)

mixed_tuple=(1,2,['a','b'])

print(a_tuple)
print("mixed_tuple: " + str(mixed_tuple))

mixed_tuple[2][0]='c'

print("mixed_tuple: " + str(mixed_tuple))