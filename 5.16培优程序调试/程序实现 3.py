s="CixiStudent"
f=[0]*26
t=s[4:]
i=0
while i<len(t):
    zm=ord(t[i])-ord('a')
    if "A"<=t[i]<="Z":
        i+=1
        continue
    elif "a"<=t[i]<="z" and f[zm]==0:
        f[zm]+=1
    i+=1
for i in range(26):
    if f[i]==1:
        print(chr(i+ord('a')),end='')