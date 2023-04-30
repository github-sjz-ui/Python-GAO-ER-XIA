def mjg(s):
    st=[]
    kh='{[()]}'
    opp={')':'(',']':'[','}':'{'}
    for i in s:
        if i in kh[:3]:
            st.append(i)
        elif i in kh[3:]:
            if len(st)==0 or opp[i]!=st.pop():
                return False
    else:
        return len(st)==0

ss='{a/[(b-c)[]{()}()+d]}*e' #input('输入数学计算式：')
if mjg(ss):
    print('括号匹配')
else:
    print('括号不匹配')
