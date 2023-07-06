from random import randint
n=10
data=[randint(10,90) for i in range(n)]
print('原始随机数：',data)

#大小交替排序
#冒泡
def bubblesort(d):
    f=1
    for i in range(n-1):
        for j in range(n-1,i ,-1):
            if d[j]*f < d[j-1]*f:
                d[j],d[j-1]=d[j-1],d[j]
        f=-f
    print('冒泡：',d)
    
#选择
def selectsort(d):
    f=1
    for i in range(n-1):
        k=i
        for j in range(i+1,n):
            if d[j]*f > d[k]*f:
                k=j
        if k!=i:
            d[k],d[i]=d[i],d[k]
        f=-f
    print('选择：',d)

bubblesort(data)
selectsort(data)