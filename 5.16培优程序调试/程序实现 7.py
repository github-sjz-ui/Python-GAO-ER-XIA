def xtod(s,m):#将 m 进制数 s 转换为十进制数 
    n=len(s);y=0 
    for k in range(0,n): 
        ch3=s[k] 
        if "F">=ch3>="A": 
            x=ord(ch3)-55 
        else: 
            x=int(ch3) 
        y= y*m+x
    return y 
s1=input("请输入式子:")
i=0;ans=0 
dic={"B":2,"D":10,"H":16} 
for j in range(0,len(s1)): 
    ch1=s1[j] 
    ch2=s1[j-1] 
    if ch1=="+" or ch1=="=": 
        s2=s1[i:j-1] 
        ans=ans+xtod(s2,dic[ch2])
        i=j+1
print("运算结果为:"+str(ans)+"D")
