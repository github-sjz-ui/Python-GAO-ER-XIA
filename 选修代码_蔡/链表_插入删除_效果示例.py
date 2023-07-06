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

def insert_pos(head,pos):
    p=head;c=1
    while c!=pos and p!=-1:
        pre=p
        p=data[p][1]
        c+=1
    if p==head:					#头节点前
        data.append([newd,head])
        head=len(data)-1
    else:						#pre节点后插入
        data.append([newd,data[pre][1]])
        data[pre][1]=len(data)-1
    return head

#初始化并输出  
data=[['d8',-1],['d3',7],['d1',6],['d6',5],['d5',3],['d7',0],['d2',1],['d4',4]]
head=2
for i in range(len(data)):
    print(i,data[i])
i=head
while i!=-1:
    print(data[i][0],end=' -> ')
    i=data[i][1]
             
while True:	#系统执行
    print()
    cho=input('===请输入您的操作数字（1-删除；2-插入；其他-退出）：')
    if cho=='1':
        deld=input('===请输入您要删除的数据:')
        head=del_value(head,deld)
    elif cho=='2':
        newd='new' #input('请输入您要插入的数据:')
        inpos=int(input('===请输入您要插入的位置:'))
        head=insert_pos(head,inpos)
    else:
        print('===!已退出!===')
        break
    
    #访问输出执行结果
    i=head
    while i!=-1:
        print(data[i][0],end=' -> ')
        i=data[i][1]
