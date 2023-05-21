data=[180,283,385,170,276,384,180,285,380,190,295,390,170,272,372]
s=[0,0,0]  #存储3个作品的得分
ans=[]  #存储并列最高平均分的作品号
maxb=0
for i in range(len(data)):
    zp=data[i]//100 		#分离出作品编号
    fs=data[i]%100		#分离出作品得分
    s[zp-1]+=fs			#累加当前作品的得分
for j in range(3):
    s[j]=s[j]/5
    print('作品',j+1,'平均分为：',s[j])
    if s[j]>maxb:
        maxb=s[j]
for z in range(3): 	#查找并列最高平均分
    if s[z]==maxb:
        ans.append(z+1)	#将数据添加到列表ans尾部
print('平均分最高的作品号是：',ans)
