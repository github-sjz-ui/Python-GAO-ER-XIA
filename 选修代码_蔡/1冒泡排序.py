from random import randint
n=10
data=[randint(10,90) for i in range(n)]
print('原始随机数：',data)

#向前冒泡
def sortup(d):
    for i in range(n-1):
        for j in range(n-1,i ,-1):
            if d[j] < d[j - 1]:
                d[j],d[j - 1]=d[j - 1],d[j]
    print('向前：',d)
#向后冒泡
def sortdown(d):
    for i in range(n-1):
        for j in range(n-1-i):
            if d[j] < d[j + 1]:
                d[j],d[j + 1]=d[j + 1],d[j]
    print('向后：',d)

sortup(data)
sortdown(data)