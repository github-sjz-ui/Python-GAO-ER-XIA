from random import randint
n=10
data=[randint(10,90) for i in range(n)]
print('原始随机数：',data)

#两端同时交换（单序）
def sortsame(d):
    lt=0;rt=n-1
    while lt<rt:
        imin=lt;imax=rt
        for i in range(lt,rt+1):
            if d[i]<d[imin]:
                imin=i
            if d[i]>d[imax]:
                imax=i
        d[imin],d[lt]=d[lt],d[imin]
        if imax==lt:
            imax=imin
        d[imax],d[rt]=d[rt],d[imax]
        lt+=1;rt-=1
    print(d)
    
#两端交替上升
def sortturn1(d):
    lt=0;rt=n-1;flag=True
    while lt<rt:
        k=lt
        for i in range(lt+1,rt+1):
            if d[i]<d[k]:
                k=i
        if flag:
            d[k],d[lt]=d[lt],d[k]
            lt+=1
        else:
            d[k],d[rt]=d[rt],d[k]
            rt-=1
        flag=not flag
    print('两端交替上升',d)

def sortturn2(d):
    st=0;ed=n-1;f=1
    while st!=ed:
        k=st
        for i in range(st+f,ed+f,f):
            if d[i]<d[k]:
                k=i
        if k!=st:
            d[k],d[st]=d[st],d[k]
        st+=f
        st,ed=ed,st
        f=-f
    print('两端交替上升',d)
    
sortturn2(data)