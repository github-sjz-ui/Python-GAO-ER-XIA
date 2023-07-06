#书本P37合并两个有序序列，改

from random import randint
def rndsq(n):
    sq=[0]*n
    sq[0]=randint(95,100)
    for i in range(1,n):
        sq[i]=sq[i-1]-randint(1,5)
    return sq
a=rndsq(20)
print('原始数据序列一为：',a)
b=rndsq(15)
print('原始数据序列二为：',b)

def mergesq(a,b): #静态数组
    i=j=k=0
    c=[0]*(len(a)+len(b))
    while(i<len(a) and j<len(b)):
        if a[i]>=b[j]:
            c[k]=a[i]
            i+=1
            k+=1
        else:
            c[k]=b[j]
            j+=1
            k+=1
    while i<20:
        c[k]=a[i]
        i+=1
        k+=1
    while j<15:
        c[k]=b[j]
        j+=1
        k+=1
    return c

def mergesqap(a,b): #动态数组
    i=j=0
    c=[]
    while(i<len(a) and j<len(b)):
        if a[i]>=b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    c=c+a[i:]+b[j:]
    return c

print('合并后的数据序列为：',mergesqap(a,b))
