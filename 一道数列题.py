'''
一道数学题：
an=an-1 - an-2
'''
def f(a1,a2,n):#a1为第一项,a2为第二项,n为第n项
    if n==1:
        return a1
    elif n==2:
        return a2
    else:
        return f(a1,a2,n-1)-f(a1,a2,n-2)
a1=int(input())
a2=int(input())
n=int(input())
for i in range(1,n+1):
    print(f(a1,a2,i))