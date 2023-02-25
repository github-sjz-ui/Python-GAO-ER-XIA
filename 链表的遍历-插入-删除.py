# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:50:20 2023

@author: HP
"""

a=[["苏州",3],["北京",-1],["上海",0],["南京",1],["武汉",2]]
head=4
pre=2
a.append(["江西",a[pre][1]])
a[pre][1]=len(a)-1
print(a)


#从头部插入新节点
a.append(["浙江",head])
head=len(a)-1
print(a)

#从尾部插入新节点
p=head
while a[p][1]!=-1:
    p=a[p][1]
a.append(["新疆",-1])
a[p][1]=len(a)-1

#删除头部节点
head=a[head][1]

#删除中间节点
pre=5
p=a[pre][1]
a[pre][1]=a[p][1]
#删除尾节点
p=head 
while a[p][1]!=-1:
    pre=p
    p=a[p][1]
a[pre][1]=-1


#遍历
p=head
while a[p][1]!=-1:
    print(a[p][0] ,end="->")
    p=a[p][1]
print(a[p][0])
