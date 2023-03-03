data=[['d8',-1],['d3',7],['d1',6],['d6',5],['d5',3],['d7',0],['d2',1],['d4',4]]
head=2

#方法一
i=head
while i!=-1:
    print(data[i][0],end=' -> ')
    i=data[i][1]
        
print()   #换行

#方法二
p=head
while data[p][1]!=-1:
    print(data[p][0],end=' -> ')
    p=data[p][1]
print(data[p][0])
