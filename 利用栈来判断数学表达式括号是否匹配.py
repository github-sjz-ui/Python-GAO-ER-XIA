n="((1*4)+6)/(4-5))("
def check_1(n):
    count_1=0
    count_2=0
    for i in n:
        if i=="(":
            count_1+=1
        if i==")":
            count_2+=1
    if count_1==count_2:
        return True
    return False
def check_2(n):
    top=-1
    for i in n:
        if i=="(":
            top+=1
        if i==")":
            top-=1
        if top<-1:
            return False
    if top==-1:
        return True
    return False
print('check_1:',check_1(n))
print('check_2:',check_2(n))
print(check_1(n) and check_2(n))
