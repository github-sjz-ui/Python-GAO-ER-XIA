import random
n=100000 # 产 生 n 个 点
ns=0
def judge(x,y):
    flag = False
    if  x*x+y*y <1:
        flag = True
    return flag
i=1
while i<=n :
    x=random.uniform(0, 1)  #产生 [0,1] 范围内的实数
    y=random.uniform(0, 1)
    if judge(x,y):
        ns+=1
    i+=1
print("圆周率的近似值 :",4*ns/n)
