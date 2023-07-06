data=[['d8',2],['d3',7],['d1',6],['d6',5],['d5',3],['d7',0],['d2',1],['d4',4]]
head=2

for i in range(len(data)):
    print(i,data[i])

i=head;c=0
while c<len(data)*2:
    print(data[i][0],end=' ')
    i=data[i][1]
    c+=1
    

