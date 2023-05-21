n=int(input("请输入训练天数："))
sumx=0	#当前训练的踢毽子总数
t=0		#当前训练的总天数
x=0
while t<=n:
    x+=1
    t+=x
    sumx+=x**2
sumx=sumx-x*(t-n)
print('您在',n,'天中共踢了',sumx,'个毽子')