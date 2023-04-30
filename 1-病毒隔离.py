import random
n=10
s=[[0 for i in range(n)]for j in range(n)]
for i in range(n):
    #for j in range(i,n):
    for j in range(i+1):
        if i==j:
            s[i][j]=1
        else:
            s[i][j]=random.randint(0,1)
            s[j][i]=s[i][j] #①

#################     输出矩阵   ####################
print(' ',' '.join(str(m) for m in range(n)))
k=0
for i in s:
    print(str(k),' '.join(str(m) for m in i))
    k+=1
###################################################
    
bh=int(input("请输入具有病毒的人员编号:"))
gl=[False]*n
que=[-1]*n;head=0;tail=0
que[tail]=bh;tail=tail+1;gl[bh]=True
zj=True
while head<tail:
    c=que[head]
    head=head+1
    for i in range(n):  #②
        if s[c][i]==1 and c!=i:
            if zj==True:
                que[tail]=i     #③
                tail=tail+1
            gl[i]=True
    zj=False
print("需要隔离的人员编号为：")
for i in range(n):
    if gl[i]==True:
        print(i,end=" ")
