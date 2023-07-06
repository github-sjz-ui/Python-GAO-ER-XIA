from random import randint
data=[]
head=-1
tmp=randint(95,99)
data.append([tmp,head])
head=0
for i in range(1,5):
    tmp=data[i-1][0]-randint(5,9)
    data.append([tmp,data[i-1][1]])
    data[i-1][1]=i

print(data)