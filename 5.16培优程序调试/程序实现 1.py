import random
s=input('请输入大写字母字符串：')
k=key=miw=""
for j in range(4):
    k='9113'#k+str(random.randint(1,9))
print('随机生成的密钥：'+k)
for i in range(len(s)):
    zm=s[i]
    key=int(k[i%len(k)])
    t=(ord(zm)-ord('A')-key)%26+ord('A')
    miw=chr(t)+miw
print("加密后的密文："+miw)