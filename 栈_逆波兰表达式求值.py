def postorde2(ss):
    st=[]
    for i in ss:
        if '0'<=i<='9':
            st.append(i)
        else:
            a=st.pop()
            b=st.pop()
            st.append(str(eval(b+i+a)))
    return st[0]

def postorde1(ss):
    st=[None]*100
    top=-1
    for i in ss:
        if '0'<=i<='9':
            top+=1
            st[top]=int(i)
        else:
            a=st[top]
            top-=1
            b=st[top]
            if i =='-':
                st[top]=b-a
            if i =='+':
                st[top]=b+a
            if i =='*':
                st[top]=b*a
            if i =='/':
                st[top]=b/a
    return st[0]

s='682-2*3/+'
print(postorde1(s),postorde2(s))