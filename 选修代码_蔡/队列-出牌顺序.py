s='234567890JQKA'
que=['']*300 
head=0
tail=0
for i in range(len(s)):
    que[tail]=s[i]
    tail+=1
    
#出1张，1张放后面，出2张，1张放后面，出3张，1张放后面……
def cp1(q,head,tail):
    c=1;res='';i=0
    while head!=tail:
        res+=q[head]
        head+=1
        i+=1
        if i==c and head!=tail:
            q[tail]=q[head]
            tail+=1
            head+=1
            c+=1
            i=0
        
    return res
   
#出1张，1张放后面，出1张，2张放后面，出1张，3张放后面……   
def cp2(q,head,tail):
    c=1;res=''
    while head!=tail:
        res+=q[head]
        head+=1
        if head!=tail:
            for i in range(c%(tail-head)):
                q[tail]=q[head]
                tail+=1
                head+=1
        c+=1
    return res 
print ('出1-n张，放1:',cp1(que,head,tail))
print ('出1，放1-n张:',cp2(que,head,tail))
