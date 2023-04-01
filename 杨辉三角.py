a=[[0 for i in range(30)]for j in range(300)]
n=int(input("输入要打印杨辉三角形的行数:"))
for i in range(n):
    for j in range(i+1):
        if i<=1:
            a[i][j]=1
        elif j>0 and j!=i:
            a[i][j]=a[i-1][j-1]+a[i-1][j]
        else:
            a[i][j]=1
for i in range(n):
    for j in range(i+1):
        print(a[i][j],end=" ")
    print()