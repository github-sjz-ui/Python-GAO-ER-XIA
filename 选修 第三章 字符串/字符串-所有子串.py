s=input(' input a string:')
n=len(s)
a=[];b=[];c=[]

for i in range(len(s)): #左边界
    for j in range(1,len(s)+1-i): #取长度
        a.append(s[i:i+j])
print(a)

for i in range(1,n+1): #取长度
    for j in range(0,n-i+1):  #左边界
        b.append(s[j:j+i]) 
print(b)

for i in range(n):  #左边界
    for j in range(i+1,n+1):  #右边界
        c.append(s[i:j])
print(c)