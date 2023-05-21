i,flag=100,False
while i>0 and not flag:
    i-=1
    j=90065+i*100
    if (j%37)*(j%67)==0:flag=True
print(i,j)