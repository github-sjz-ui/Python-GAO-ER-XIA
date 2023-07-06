from random import randint
n=10
data=[randint(10,90) for i in range(n)]
print('原始随机数：',data)

#冒泡变式
def sortt(d):
    for i in range(n-1):
        for j in range(n-1,i ,-1):
            if d[j] < d[i]:
                d[j],d[i]=d[i],d[j]
    print('变式：',d)
    
#前
def sortup(d):
    for i in range(n-1):
        k=i
        for j in range(i+1,n):
            if d[j] < d[k]:
                k=j
        if k!=i:
            d[k],d[i]=d[i],d[k]
    print('向前：',d)
    
#后
def sortdown(d):
    for i in range(n-1,0,-1):
        k=i
        for j in range(i):
            if d[j] > d[k]:
                k=j
        if k!=i:
            d[k],d[i]=d[i],d[k]
    print('向后：',d)

sortdown(data)