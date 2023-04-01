# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 21:28:39 2023

@author: HP
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df2=pd.read_excel("16高二下一月考.xlsx")
df=pd.read_excel("高二期末成绩20030212.xlsx")
name='沈纪中'
# 判断选科
all_xuanke=['语文','数学','英语','物理','化学','生物','政治',\
           '历史','地理','技术']
score=[]
name=df[df.姓名==name]
xk=[]
list=['语名','数名','英名','物名','化名','生名',\
               '政名','历名','地名','技名'] 
for i in all_xuanke:
    if float(name[i])>0:
        xk.append(i)
        number=df[i].count()-(df[i]==0).sum()
        k=int(name[list[all_xuanke.index(i)]])
        score.append(1-k/number)
        print(score)
'''
for i in all_xuanke:
    if not name[i].empty:
        xk.append(i)
        number=df[i].count()-(df[i]==0).sum()
        score.append(1-int(name[list[all_xuanke.index(i)]])/number)
'''

score1=[42,259,23,106,214,30,136,18]#前一阶段的所有成绩排名最后一位为年级排名倒数第二为班级排名

xuanke=["语文","数学","英语","物理","化学","技术","年级排名","班级排名"]
score2=[568,144,55,100,69,3,70,7]#后一阶段的所有成绩排名
res1=0;res2=0#1为记录进步情况2为反之
for i in range(8):
    if score1[i]>score2[i]:
        res1+=1#作为比较成绩总体进步情况的变量
        a=(score1[i]-score2[i])/score1[i]
        if a>=0.3:
            print(xuanke[i]+"进步了一点，进步了"+str(a)[:4]+"进步了"+str(score1[i]-score2[i])+"名")
        elif a>=0.6:
            print(+xuanke[i]+"进步较为明显，进步了"+str(a)[:4]+"进步了"+str(score1[i]-score2[i])+"名")	
        elif a>=0.9:
            print(+xuanke[i]+"进步较为显著，进步了"+str(a)[:4]+"进步了"+str(score1[i]-score2[i])+"名")
    else:
        res2+=1
        b=score2[i]-score1[i]
        print(xuanke[i]+"退步了"+str(b)+"名哦,继续努力")

if res1>=3:
	print("本次成绩总体进步较大")
	if res1<3:
		print("本次成绩仍还有进步空间")
elif res2>=4:
		print("本次退步幅度较大应该注重关注")
		if res2<3:
			print("仍需努力")





# 绘制六维雷达图
# 用于正常显示中文
plt.rcParams['font.sans-serif'] = 'SimHei'
#用于正常显示符号
plt.rcParams['axes.unicode_minus'] = False
 # 使用ggplot的绘图风格，这个类似于美化了，可以通过plt.style.available查看可选值，你会发现其它的风格真的丑。。。
plt.style.use('ggplot')
plt.figure(dpi=800,figsize=(24,8))
data = score#输入六门成绩
angles=np.linspace(0, 2*np.pi, 6, endpoint=False)
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'bo-', linewidth=2)
ax.fill(angles, data, facecolor='r', alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, [xk[0],xk[1],\
                 xk[2],xk[3],xk[4],xk[5]])
ax.grid(True)
plt.show()




            
