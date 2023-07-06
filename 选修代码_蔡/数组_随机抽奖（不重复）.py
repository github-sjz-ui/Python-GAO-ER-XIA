#参考书本P39-40的摇号系统，用数组实现自己班级同学名单的抽奖程序。

from random import randint

csv_file=open('36名单.csv','r')	    #打开名单文件
flines=csv_file.readlines()		#将文件中的姓名按行读入flines列表
csv_file.close()				#关闭文件
luck=['']*len(flines)			#初始化一个包含学生人数个数据元素的数组
i=0
for i in range(len(flines)):
    tmp=flines[i].strip('\n')		#将一个编号去除换行后赋给tmp
    luck[i]=tmp				#按读取顺序将姓名赋值给数组元素luck[i]
m=int(input('输入抽奖人数：'))
c=0
while c<m:
    k=randint(0,len(luck)-1)
    if luck[k]!="":			#判断luck[k]是否已被抽取
        c+=1
        print(luck[k])
        luck[k]=""			#表示该位置姓名已被抽取
