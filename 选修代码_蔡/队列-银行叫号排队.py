que=[0]*1000
head=tail=0
print('1.取号； 2.叫号； 3.退出')
x=int('0'+input('请输入操作编号：'))

while x!=3:
    if x==1:
        que[tail]+=1
        print('您的号：A%d，前面还有%d人'%(tail,tail-head))
        tail+=1
    elif x==2:
        if head==tail:
            print('没有客户了')
        else:
            print('请A%d到窗口办理业务'%(head))
            head+=1
    else:
        print('操作编号错误，请重新输入')
        
    x=int('0'+input('请输入操作编号：'))
else:
    tot=sum(que)-(tail-head)
    print('今日业务办理人数：',tot)