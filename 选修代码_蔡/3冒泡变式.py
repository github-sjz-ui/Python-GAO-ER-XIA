from random import randint
n=7
data=[randint(10,90) for i in range(n)]
print('原始随机数：',data)

#奇偶索引位置分别排序（同序）-向前冒泡
def ups(d):
    for i in range(n-1):
        for j in range(n-1,i+1 ,-1):
            if d[j] < d[j - 2]:
                d[j],d[j - 2]=d[j - 2],d[j]
    print('向前同序：',d)
    
#奇偶索引位置分别排序（同序）-向后冒泡
def downs(d):
    for i in range(n//2):
        for j in range(n-2*(i+1)):
            if d[j] < d[j + 2]:
                d[j],d[j + 2]=d[j + 2],d[j]
    print('向后同序：',d)

#奇偶索引位置分别排序（异序）-向前冒泡
def upd(d):
    for i in range(n-1):
#        k=1
        for j in range(n-1,i +1,-1):
            if j %2 == 1 and d[j] < d[j - 2] or j %2 == 0 and d[j] > d[j - 2] :
#            if d[j] *k < d[j - 2] *k:
                d[j],d[j - 2]=d[j - 2],d[j]
#            k=-k
    print('向前异序：',d)
    
#奇偶数值分别排序（奇数排前）-向前冒泡
def upnum(d):
    for i in range(n-1):
        for j in range(n-1,i ,-1):
            if d[j] %2 == d[j - 1]%2:
                if d[j]<d[j-1]:
                    d[j],d[j - 1]=d[j - 1],d[j]
            elif d[j]%2 ==1:
                d[j],d[j - 1]=d[j - 1],d[j]
            #if d[j] %2 == d[j - 1]%2 and d[j]<d[j-1] or d[j] %2 > d[j - 1]%2:
                
    print('奇偶数值排序：',d)   
upd(data)