s='0'+input()+'0'
c=0;i=2
n=len(s)-1
while i<n:
    if s[i]=='1':
        i=i+2
    elif s[i-1]=='1':
        i=i+1
    elif s[i+1]=='1':
        i=i+3
    else:
        s=s[:i]+'1'+s[i+1:]
        c=c+1
print('最多可翻转',str(c),'个')