from random import randint

def rnddata(n):			    #产生随机数值的降序链表
    data=[]
    head=-1
    tmp=randint(95,99)
    data.append([tmp,head])
    head=0
    for i in range(1,n):
        tmp=data[i-1][0]-randint(1,5)
        data.append([tmp,data[i-1][1]])
        data[i-1][1]=i
    return data
a=rnddata(5)
b=rnddata(6)
print('序列一：',a,'\n序列二：',b)

ka=qa=kb=heada=headb=0		#初始化所有指针位置
while ka!=-1 and kb!=-1:
    if a[ka][0]>b[kb][0]:
        qa=ka
        ka=a[ka][1]
    else:
        if ka==heada:				#插入在头节点前
            a.append([b[kb][0],heada])
            heada=len(a)-1
        else:					#插入在其他节点前
            a.append([b[kb][0],ka])
            a[qa][1]=len(a)-1
        qa=len(a)-1
        kb=b[kb][1]
while kb!=-1:					#a链表结束，b链表还有数据
    a.append([b[kb][0],-1])
    a[qa][1]=len(a)-1
    qa=a[qa][1]
    kb=b[kb][1]
print('合并后的存储结构:',a)
print('链表逻辑结构: head=',heada)
p=heada
while p!=-1:
    print(a[p][0],end= ' ')
    p=a[p][1]
    
