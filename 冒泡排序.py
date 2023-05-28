# -*- coding: utf-8 -*-
"""
Created on Tue May 16 14:16:28 2023

@author: HP
"""

a=[190,188,193,186,208,185,188,184]
for j in range(1,8):
    for i in range(0,8-j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a)