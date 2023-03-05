# 随机数链表，删除所有奇数
def del_value(head,numv):
    p=head
    while data[p][0]!=numv and p!=-1:   #按数据值查找位置
        pre=p
        p=data[p][1]
    if p==head:				#删头节点
        head=data[head][1]
    else:
        data[pre][1]=data[p][1]	        #删除其他节点        
    return head

data=[[76,-1],[66,7],[85,6],[32,5],[55,3],[31,0],[34,1],[59,4]]
head=2
i=head
while i!=-1:
    if data[i][0]%2==1:
        head=del_value(head,data[i][0])
    pre=data[i][1]
    i=data[i][1]
i=head
while i!=-1:
    print(data[i][0],end=' -> ')
    i=data[i][1]
print()