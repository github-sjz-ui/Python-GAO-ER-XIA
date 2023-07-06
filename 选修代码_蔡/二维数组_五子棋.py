#判断输入坐标上是否可以落子
def jgpos(x,y):
    if x<0 or y<0 or x>g-1 or y>g-1:
        return False
    for i in range(g):
        for j in range(g):
            if qipan[x][y]!=0:
                return False
    return True

#判断输赢
def jgfinish(x,y):
    count1=count2=count3=count4=1
    
    #横向—
    i=j=y
    while count1<5:
        if  i>0 and qipan[x][i-1]==qipan[x][i]:
            i-=1
            count1+=1
        elif  j<g-1 and qipan[x][j+1]==qipan[x][j]:
            j+=1
            count1+=1
        else:
            break
        
    #纵向|
    i=j=x
    while count2<5:
        if i>0 and qipan[i-1][y]==qipan[i][y]:
            i-=1
            count2+=1
        elif j<g-1 and qipan[j+1][y]==qipan[j][y]:
            j+=1
            count2+=1
        else:
            break
            
    #左上右下\
    i=j=x; m=n=y
    while count3<5:  
        if  i>0 and m>0 and qipan[i-1][m-1]==qipan[i][m]:
            count3+=1
            i-=1;m-=1
        elif j<g-1 and n<g-1 and qipan[j+1][n+1]==qipan[j][n]:
            count3+=1
            j+=1;n+=1
        else:
            break
        
    #左下右上/
    i=j=x; m=n=y
    while count4<5:  
        if i<g-1 and m>0 and qipan[i+1][m-1]==qipan[i][m]:
            count4+=1
            i+=1;m-=1
        elif j>0 and n<g-1 and qipan[j-1][n+1]==qipan[j][n]:
            count4+=1
            j-=1;n+=1
        else:
            break
                
    if count1>=5 or count2>=5 or count3>=5 or count4>=5:
        return True

#初始化棋盘
g=5
emp=g*g   
qipan=[[0 for i in range(g)]for j in range(g)]
for i in range(g):
    print(qipan[i])
pdic={1:'黑方',2:'白方'}

c=0
while True:
    #落子：
    try:
        new=list(map(int,input(pdic[c%2+1]+'落子，请输入行列坐标(x,y) ：').split(',')))
        while not jgpos(new[0],new[1]):
            print('该位置不能落子，请重下：')
            new=list(map(int,input(pdic[c%2+1]+'落子，请输入行列坐标(x,y)：').split(',')))
    except:
        print('坐标输入错误，请重下：')
        continue
    qipan[new[0]][new[1]]=c%2+1
    emp-=1
    for i in range(g):
        print(qipan[i])
        
    #判断输赢：
    if jgfinish(new[0],new[1]):
        print(pdic[c%2+1]+'获胜')
        break
    elif emp==0:
        print('平局')
        break  
    c+=1
       