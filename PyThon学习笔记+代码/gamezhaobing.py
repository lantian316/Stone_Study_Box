#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2017/2/3-10:25.
Author:Stone
Email:lantian316@163.com
企鹅:283302410
'''

#按照 粮食、木头、石头、铁矿 排序
hanzi=['粮食','木头','石头','铁矿']
xianyou=[8.550,10.800,3.920,8.000]
sudu=[2.360,1.810,1.300,0.297]
zongshu=[]
chaliang=[]

for j in range(4):
    zongshu.append(xianyou[j]+sudu[j]*8)

print("最大值为：" + str(max(zongshu)))

for j in range(4):
    chaliang.append(max(zongshu)-zongshu[j])

print(chaliang)




