lst=[]
n=int(input("请输入参与人数："))
m=int(input("请输入报数数字："))
for i in range(n-1):
    lst.append([i+1,i+1])
lst.append([n,0])

head=0;long=n;k=head
i=1
while long>1:
    i+=1
    if i==m:
        t=lst[k][1]
        lst[k][1]=lst[t][1]
        if t==head:
            head=lst[k][1]
        i=1
        long=long-1
    k=lst[k][1]
print("最终剩下的人的编号",lst[head][0])
