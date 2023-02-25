# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 12:35:57 2023

@author: HP
"""
'''
sum=0
#数组去重，方法一
a=[3,5,3,2,1,5,4]
i=0
while i <len(a):
    for j in range(len(a)-1,i,-1):
        sum+=1
        if a[j]==a[i]:
            a.pop(j)
    i+=1
print(a,sum)
'''
#数组元素去重，方法二
a=[3,5,3,3,3,2,1,5,4]
print(a)
i,n=0,len(a)
while i<n:
    c=0
    for j in range(i+1,n):
        if a[j]==a[i]:
            c+=1
        else:
            a[j-c]=a[j]
    n-=c
    i+=1
    print(a)
del a[n:]
print(a)
'''
a=[3,5,3,2,1,5,4]
i,n=0,len(a)
while i<n:
    r=i+1
    for j in range(r,n):
        if a[j]!=a[i]:
            a[r]=a[j]
            r+=1
    print(a)
    n=r
    i+=1
del a[n:]
print(a)
'''








