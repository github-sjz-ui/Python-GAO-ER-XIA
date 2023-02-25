# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:03:54 2023

@author: HP
"""

list=[]
n=int(input("请输入参与人数："))
m=int(input("请输入报数数字："))
for i in range(n-1):
    list.append([i+1,i+1])
list.append([n,0])
head=0
long=n
k=head
i=1

while long>1:
    i+=1
    if i==m:
        t=list[k][1]
        list[k][1]=list[t][1]
        if t==head:
            head=list[k][1]
        i=1
        long=long-1
    k=list[k][1]
print("最终剩下的人的编号",list[head][0])