s='abcdefghij'
c=input('zic:')
#1.成员运算符 in
if c in s:
    print('Y')
else:
    print('N')
    
#2.遍历+切片
for i in range(len(s)):
    if s[i:i+len(c)]==c:
        print('Y')
        break
else:
    print('N')
    
#3
for i in range(len(s)):
    if c[0]==s[i]:  #找到c首字符位置
        j=1
        while j<len(c) and c[j]==s[i+j]: #往后找相等部分
            j+=1
        if j==len(c):  #找完c长度表示是子串
            print('Y')
            break
else:
    print('N')