from random import randint
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #中文显示
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(12.8,7.2),dpi=800)
tmp={}
for i in range(1000):
    n=randint(0,1000)
    if n in tmp:
        tmp[n]+=1
    else:
        tmp[n]=1

df1 = pd.DataFrame(tmp,index=[0]).T
x=df1.index
y=df1[0]
plt.bar(x,y,label="频率")
plt.title("次数")
plt.xlabel("数")
plt.ylabel("次数")
plt.legend()
plt.savefig('随机数.png')
plt.show()
df1.to_excel('随机数.xlsx')