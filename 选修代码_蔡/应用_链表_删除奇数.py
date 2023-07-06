from random import randint

#输出链表
def print_list(li,p):
    while p!=-1:
        print(li[p][0],end=' -> ')
        p=li[p][1]   #1
    print()

#创建随机数值链表
data=[]
head=0
p=-1
n=int(input('链表的长度：'))
for i in range(n):
    node=[randint(10,99),-1]
    data.append(node)
    if p!=-1:
        data[p][1]=len(data)-1  #2
    p=len(data)-1
print(data)
print_list(data,head)

#删除奇数
p=head
while data[p][0]%2==1 and p!=-1:  #删头节点
    p=data[p][1]
    
head=q=p
while p!=-1:
    if data[p][0]%2==1:
        data[q][1]=data[p][1] #3
    else:
        q=p
    p=data[p][1]

print('新链表:')
print_list(data,head)
