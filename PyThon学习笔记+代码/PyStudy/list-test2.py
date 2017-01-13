#  -*- coding:utf-8 -*-

number_list=[1,3,5,7,9]
string_list=["what","java",7878,343]
string_list1=["what","java","sldjf","kjdkf"]

print(len(number_list))
print(len(string_list))#列表中元素个数
print(max(number_list))#返回列表中最大的值
print(max(string_list1))
print(min(number_list))#返回列表中最小的值
print(min(string_list1))

print(number_list,string_list,string_list1)

number_list.append(18)#在列表末尾添加新的对象
string_list.append("18")
string_list1.append("what are you doing")
string_list1.append("what")
print(number_list,string_list,string_list1)
print(string_list1.count("what"))#统计某个元素在列表中出现的次数
string_list.extend(number_list)#在列表末尾一次性追加另一个序列中的多个值
print(string_list)
print(number_list.index(3))#从列表中找出某个值第一个匹配项的索引位置
number_list.insert(6, 876876)#将对象插入列表
print(number_list)
print(number_list.pop())#移除列表中的一个元素，默认最后一个，并返回该元素（被移除的元素）
print(number_list)
number_list.remove(1)#移除列表中某一个值的第一个匹配项
print(number_list)
number_list.reverse()#反向列表中元素（颠倒）
print(number_list)
number_list.sort()#对原列表进行排序
print("paixu" + str(number_list))

# print(cmp(number_list,string_list))

# print(cmp([1,2],[1,2]))