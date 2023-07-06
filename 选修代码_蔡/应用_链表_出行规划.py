def del_value(head,numv):
    p=head
    while data[p][0]!=numv and p!=-1:
        pre=p
        p=data[p][1]
    if p==head:				#删头节点
        head=data[head][1]
    elif p==-1:				#没找到
        print('not found')
    else:
        data[pre][1]=data[p][1]	#删除其他节点        
    return head

def insert_pos(head,x,pos):
    p=head
    while data[p][0]!=pos and p!=-1:
        pre=p
        p=data[p][1]
    if p==head:					#头节点前
        data.append([x,head])
        head=len(data)-1
    else:						#pre节点后（p节点前）插入
        data.append([x,data[pre][1]])
        data[pre][1]=len(data)-1
    return head

#初始化链表并输出  
data=[['杭州',1],['北京',-1]]
head=0
i=head
while i!=-1:
    print(data[i][0],end=' -> ')
    i=data[i][1]
             
while True:	#系统执行
    print()
    cho=input('===请输入您的操作数字（1-删除；2-插入；其他-退出）：')
    if cho=='1':
        deld=(input('===请输入您要删除的地点(以空格分隔)：')+' ').split()
        for i in deld:  
            head=del_value(head,i)
    elif cho=='2':
        inpos=input('===在哪个地点前面插入新地点(插入终点站请直接回车)：')
        newd=(input('===请输入您要插入的地点(以空格分隔)：')+' ').split()
        for i in newd:
            head=insert_pos(head,i,inpos)
    else:
        print('===!已退出!===')
        break
    
    #访问输出执行结果
    i=head
    while i!=-1:
        print(data[i][0],end=' -> ')
        i=data[i][1]
