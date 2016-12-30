#  -*- coding:utf-8 -*-


print("立刻对减肥\nhow are you?\nfine")
number_list=[1,3,5,7,9]
string_list=["what","java",7878,343]
print("list: "+str(number_list))

print("根据 值 查找list的下标： "+ str(number_list.index(1)))
print("根据  下标 查找list的值： "+ str(number_list[1]))

print("{0}{1}{2}".format(string_list[0], string_list[1],string_list[2]))

print("number_list的长度为：",len(number_list))
number_list[1]=18
string_list[2]="lkjskdf"
print("list: "+str(number_list))
print("list: "+str(string_list))
del number_list[1]
del string_list[1]
print("list: "+str(number_list))
print("list: "+str(string_list))
add_list=(number_list+string_list)
print("list: "+str(add_list))

print(len([1,2,3,4,5]))
print([1,2,3,4,5]+[6,7,8,9,10])
print(['hello'] * 4)
print(5 in [1,2,3,4])

abcd_list = ['a','b','c','d']
print(abcd_list[1])
print(abcd_list[-2])
print(abcd_list[1:])
print(abcd_list[2:])
print(abcd_list[:3])

