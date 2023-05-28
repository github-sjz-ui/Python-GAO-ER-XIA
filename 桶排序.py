a=[0,1,5,6,20,3,4,15,17,32,27,25,25]
b=[0]*33
for i in range(len(a)):
    b[a[i]]+=1
print(b)
for j in range(len(b)-1):
    while b[j]>0:
        print(j,end='->')
        b[j]-=1
