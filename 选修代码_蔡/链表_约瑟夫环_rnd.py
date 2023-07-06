from random import randint
lst=[]
n=int(input("请输入参与人数："))
x=randint(2,9)
for i in range(n-1):
    lst.append([i+1,i+1])
lst.append([n,0])

q=p=head=0
i=0
while n>1:
    i+=1
    if i==x:
        lst[q][1]=lst[p][1]
#        if p==head:
#            head=lst[p][1]
        print('报数x: ',x,'出列：',lst[p][0])
        i=0
        n=n-1
        x=randint(2,9)
        
    q=p
    p=lst[p][1]
#print("最终剩下的人的编号",lst[head][0])
print("最终剩下的人的编号",lst[p][0])
