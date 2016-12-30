#  -*- coding:utf-8 -*-

#创建一个字典
phone_book = {'Tom':1213123,'jerry':8789788}

mixed_dict = {"tom":'boy',11:8765786}

print(phone_book)
print(str(phone_book['Tom']))


#修改值
phone_book['Tom'] = 982798787987987987987878

print(str(phone_book['Tom']))
print(phone_book)

#添加新的键值对
phone_book['heath'] = 546545
print(phone_book)

#删除键值对
del phone_book['Tom']
print(phone_book)

#清空整个phone_book词典里的内容
phone_book.clear()
print(phone_book)

#删除整个词典（不是内容）
del phone_book
# print(phone_book)

#key是唯一的，不允许出现两个相同的key
rep_test = {1:867767,2:876876,1:46545}
print(rep_test[1])
print(rep_test)

#键必须是不可变的，可以使用数字，字符串，元组(tuple)来充当键，但是不能使用list列表
# list_dict = {[123]):"klsdjf",212:987678}
list_dict = {("sdf"):"klsdjf","212":987678}
print(list_dict)

