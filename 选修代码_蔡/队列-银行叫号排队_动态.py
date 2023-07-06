que=[];n=0
print('1.取号； 2.叫号； 3.退出')
x=int('0'+input('请输入操作编号：'))

while x!=3:
    if x==1:
        que.append(n)
        print('您的号：A%d，前面还有%d人'%(n,len(que)-1))
        n+=1
    elif x==2:
        if len(que)<1:
            print('没有客户了')
        else:
            x=que.pop(0)
            print('请A%d到窗口办理业务'%(x))
    else:
        print('操作编号错误，请重新输入')
        
    x=int('0'+input('请输入操作编号：'))
else:
    tot=n-len(que)+1
    print('今日业务办理人数：',tot)
