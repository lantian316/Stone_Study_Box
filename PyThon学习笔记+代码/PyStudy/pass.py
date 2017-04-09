#  -*- coding:utf-8 -*-


a_list = [0,1,2,3]
print("using continue:")
for i in a_list:
    if not i:
        continue
    print(i)



print("using pass")
for i in a_list:
    if not i:
        pass
    print(i)