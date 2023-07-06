from random import randint
n=5;flag=0
maze=[[randint(0,1) for i in range(n)]for j in range(n)]
maze[0][0]=maze[n-1][n-1]=1 #左上角入口和右下角出口设为通路1
for i in maze:
    print(i)
#判断坐标有效性   
def valid(maze,x,y):
    if(x>=0 and x<len(maze) and y>=0 and y < len(maze[0]) and maze[x][y]==1):
        return True
    else:
        return False
#移动
def walk(maze,x,y):
    global flag
    if x==n-1 and y==n-1: #到达出口
        print('successful!')
        flag=1
        return True
    #递归主体
    if valid(maze,x,y):
        maze[x][y]=2   #标记已走过的路
        #对四个方向依次试探
        walk(maze,x-1,y)
        walk(maze,x,y-1)
        walk(maze,x+1,y)
        walk(maze,x,y+1)
#主程序，函数调用
walk(maze,0,0)
if flag==0:
    print('no way')