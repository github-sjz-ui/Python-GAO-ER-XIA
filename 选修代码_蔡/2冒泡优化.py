from random import randint
n=6
data=[randint(10,90) for i in range(n)]
print('原始随机数：',data)

#向前冒泡+遍数优化
def sortup(d):
    c=0
    for i in range(n-1):
        c+=1;flag=False
        for j in range(n-1,i ,-1):
            if d[j] < d[j - 1]:
                d[j],d[j - 1]=d[j - 1],d[j]
                flag=True
        if not flag:
            break
    print('遍数优化：',d,'排序遍数:',c)

def sortup2(d):
    i = 1; c=0
    while i <= n-1:
        start = n-1; c+=1
        for j in range(n-1,i-1 ,-1):
            if d[j] < d[j - 1]:
                d[j],d[j - 1]=d[j - 1],d[j]
                start = j
        i = start + 1
    print('范围优化：',d,'排序遍数:',c)
    
sortup2(data)

