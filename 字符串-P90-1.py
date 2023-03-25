#删除k个字符后，构成的最小的字符串，剩余字符相对位置不变
#如'a3b3e4'，删除3个字符后，最小的字符串为'334c'

s=input(' input a string（ASCII）:')
k=int(input('删除个数k（小于s长度）:'))
t=k
while k>0:
    i=0
    while i<len(s)-1 and s[i]<=s[i+1]:
        i+=1
    s=s[:i]+s[i+1:]
    print(s)
    k-=1