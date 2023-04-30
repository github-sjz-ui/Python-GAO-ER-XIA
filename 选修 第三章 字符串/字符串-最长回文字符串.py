#1.输入一个字符串，求其中最长回文字符串
#2.将该字符串看作一个环，求环中最长回文字符串
#如：  fjhdhfjf  1.结果为 hdh  2.结果为 jffj
def is_hw(s):
    if s==s[::-1]:
        return True
    else:
        return False
    
s=input(' input a string:')
n=len(s)
ss=s+s
for i in range(n,0,-1):
#1.    for j in range(n-i+1):
#          t=s[j:j+i]
    for j in range(n):
        t=ss[j:j+i]
        if is_hw(t):
            print(t)
            break
    else:
        continue
    break
    
