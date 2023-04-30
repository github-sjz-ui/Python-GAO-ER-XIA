def is_hw(s):
    if s==s[::-1]:
        return True
    else:
        return False
    
s=input(' input a string:')
n=len(s)
hws=[]
for i in range(n):
    for j in range(i+2,n+1):  #要求长度不为1
        if is_hw(s[i:j]):
            hws.append(s[i:j])
print(hws)