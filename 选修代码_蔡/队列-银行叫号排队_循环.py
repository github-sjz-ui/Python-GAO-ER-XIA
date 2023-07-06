n=5
que=[-1]*n
head=tail=0
print('1.取号； 2.叫号； 3.退出')
x=int(input('请输入操作编号：'))
c=0
while x!=3:
    if x==1:
        if (tail+1)%n==head: #判满
            print('系统忙，请等待')
        else:               #入队
            que[tail]=c
            print('您的号：A%d，前面还有%d人'%(c,que[tail]-que[head])) #(tail-head+n)%n))
            tail=(tail+1)%n
            c+=1
    elif x==2:
        if head==tail:  #判空
            print('没有客户了')
        else:           #出队
            print('请A%d到窗口办理业务'%(que[head]))
            head=(head+1)%n
    else:
        print('操作编号错误，请重新输入')
        
    x=int(input('请输入操作编号：'))
else:
    print('总共办理业务人次：',c)
