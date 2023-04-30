pwd=input('input your password:')
n=len(pwd)
a=b=c=d=0
if n>=6:
    for i in pwd:
        if 'a'<=i<='z':
            a=1
        elif 'A'<=i<='Z':
            b=1
        elif '0'<=i<='9':
            c=1
        else:
            d=1
    if n>=12 and a+b+c+d==4:
        print('密码强度：强')
    elif a+b+c+d==1:
        print('密码强度：弱，只有一种字符')
    else:
        print('密码强度：中')
else:
    print('密码强度：弱, 长度不足')
