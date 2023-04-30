head=tail=0
q=['']*300
s='python'#input()
for i in s:
    q[tail]=i
    tail+=1
miwen=''
while head!=tail:
    miwen+=q[head]
    head+=1
    if head!=tail:
        q[tail]=q[head]
        head+=1
        tail+=1

print(miwen)